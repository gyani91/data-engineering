import csv
import os


def save_result(filename, columns, data):
    """
    Saves the result as a CSV file

    :param filename: file name for the CSV file
    :param columns: column names
    :param data: the result data to be written
    """
    with open(os.path.join("data/query_results/", filename), "w") as f:
        out = csv.writer(f)
        out.writerow(columns)

        for item in data:
            out.writerow(item)
