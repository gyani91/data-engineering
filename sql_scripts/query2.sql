SELECT itemid, locationid, transactiondate,
SUM(transferquantity)
OVER (PARTITION BY itemid, locationid ORDER BY transactionDate ROWS UNBOUNDED PRECEDING) as cumulative_quantity
FROM transaction
ORDER BY 1,2,3