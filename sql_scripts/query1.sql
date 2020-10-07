WITH days AS (
	SELECT day::date
 	FROM generate_series((select min(transactiondate) from transaction)::timestamp,
						 (select max(transactiondate) from transaction)::timestamp, '1 day'::interval) AS day
),

cumsum AS (
	SELECT itemid, locationid, transactiondate,
	SUM(transferquantity)
	OVER (PARTITION BY itemid, locationid ORDER BY transactionDate ROWS UNBOUNDED PRECEDING) as cumulative_quantity
	FROM transaction
	),

cross_sum AS (
  	SELECT m.itemid, m.locationid, d.day, m.transactiondate, m.cumulative_quantity
  	FROM days d
  	CROSS JOIN cumsum m
  	WHERE m.transactiondate <= d.day
  ),

filtered AS (
  	SELECT itemid, locationid, day AS BalanceDate,
	(ARRAY_AGG(cumulative_quantity ORDER BY transactiondate DESC))[1:1] AS InventoryBalance
  	FROM cross_sum
  	GROUP BY 1,2,3
  )

SELECT itemid, locationid, BalanceDate,
(SELECT SUM(InventoryBalance) FROM UNNEST(InventoryBalance) AS InventoryBalance) AS InventoryBalance
FROM filtered
ORDER BY 1,2,3