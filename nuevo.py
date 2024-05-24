#!/usr/bin/python
import sys
print("activado")


import csv
from dbfread import DBF


def dbf_to_csv(path):


# Set the name of the CSV file
csv_path = path[:-4] + ".csv"

# Create a DBF object, i.e., load the .dbf file into the code
dbf = DBF(path)

# Create a CSV file and fill it with dbf data
with open(csv_path, 'r', newline = '') as f:

    # Create the CSV writer
    writer = csv.writer(f)

    # Write the CSV column names
    writer.writerow(dbf.field_names)

    # Write the CSV rows
    for record in dbf:
        writer.writerow(list(record.values()))

return csv_path

dbf_to_csv('prueba.dbf')
