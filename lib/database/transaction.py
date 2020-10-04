from database.tables.transaction import Transaction


def convert_to_objects(df):
    """
    Reads rows of the dataframe and converts them into objects of Transaction class

    :param df: pandas dataframe
    """
    return [
        (Transaction(row.ItemID, row.LocationID, row.TransactionDate, row.TransferQuantity))
        for index, row in df.iterrows()
    ]
