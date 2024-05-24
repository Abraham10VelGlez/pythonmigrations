
from dbfread import DBF
from pprint import pprint

table = DBF("../m001/GC203T06.DBF",
            encoding="iso-8859-1")

table.load()

print(table.records)
