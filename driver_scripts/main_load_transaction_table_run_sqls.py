import pandas as pd
import os

from lib.database.transaction import convert_to_objects
from lib.utils.database_utils import add_to_db, execute_sql
from lib.utils.csv_utils import save_result


if __name__ == "__main__":
    # Read the data
    transactional_data = "data/inventory/inventory_movement.csv"
    transactional_df = pd.read_csv(transactional_data)

    # Splitting the data
    # index = int(0.8 * len(transactional_df.index))
    # transactional_df_init = transactional_df.iloc[:index, :]
    # transactional_df_incremental = transactional_df.iloc[index:, :]

    # Insert the data into db
    transactional_objs = convert_to_objects(transactional_df)
    add_to_db(transactional_objs)

    scripts_root = "sql_scripts/"

    # Query 1
    sql_query1 = open(os.path.join(scripts_root, "query1.sql"), "r").read()
    results1 = execute_sql(sql_query1)

    # Saving the output of the query 1 as a CSV
    columns = ["ItemId", "LocationId", "BalanceDate", "InventoryBalance"]
    save_result("results1.csv", columns, results1)

    # Query 2
    sql_query2 = open(os.path.join(scripts_root, "query2.sql"), "r").read()
    results2 = execute_sql(sql_query2)

    # Saving the output of the query 2 as a CSV
    columns = ["ItemId", "LocationId", "BalanceDate", "InventoryBalance"]
    save_result("results2.csv", columns, results2)

    # Query 3
    sql_query3 = open(os.path.join(scripts_root, "query3.sql"), "r").read()
    results3 = execute_sql(sql_query3)

    # Saving the output of the query 3 as a CSV
    columns = ["ItemId", "LocationId", "BalanceDate", "MA30"]
    save_result("results3.csv", columns, results3)
