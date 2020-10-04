import pandas as pd
import csv

from lib.database.transaction import convert_to_objects
from lib.utils.database_utils import add_to_db, execute_sql

if __name__ == "__main__":
    transactional_data = "data/inventory/inventory_movement.csv"
    transactional_df = pd.read_csv(transactional_data)

    # Splitting the data
    index = int(0.8 * len(transactional_df.index))
    transactional_df_init = transactional_df.iloc[:index, :]
    transactional_df_incremental = transactional_df.iloc[index:, :]

    # Loading initial 80% of data
    transactional_objs_init = convert_to_objects(transactional_df_init)
    add_to_db(transactional_objs_init)

    # Querying
    sql_query1 = "SELECT itemid, locationid, transactiondate, sum(transferquantity) FROM transaction GROUP BY itemid, locationid, transactiondate"
    results1 = execute_sql(sql_query1)

    # Saving the output of the query as a CSV
    with open("data/query_results/results1.csv", "w") as f:
        out = csv.writer(f)
        out.writerow(["itemid", "locationid", "transactiondate", "transferquantity"])

        for item in results1:
            out.writerow([item[0], item[1], str(item[2]), item[3]])
