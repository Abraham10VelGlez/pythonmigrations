#!/usr/bin/python
""" PROBADOR DE DBF A CSV STUDIO A"""
import sys
import csv
from dbfread import DBF


table = DBF('m125/GC203T04.dbf',encoding='latin_1')
writer = csv.writer(sys.stdout)

writer.writerow(table.field_names)
for record in table:
    writer.writerow(list(record.values()))
    #print( str(int(record["DESNIVEL"])) )
"""

    str(record["MUNICIPIO"]) + ' ' +
      str(record["ZONA"]) + ' ' +
      str(record["MANZANA"]) + ' ' +
      str(record["LOTE"]) + ' ' +
      str(record["TIPOPREDIO"]) + ' ' +
      str(record["REGPROP"]) + ' ' +
      str(record["DOMICILIO"]) + ' ' +
      str(record["ZONAORIG"]) + ' ' +
      str(record["CODCALLE"]) + ' ' +
      str(record["NUMEXT"]) + ' ' +
      str(record["COLONIA"]) + ' ' +
      str(record["CODPOST"]) + ' ' +
      str(record["ENTCALLE"]) + ' ' +
      str(record["YCALLE"]) + ' ' +
      str(float(int(record["SUPTERRTOT"]))) + ' ' +
      str(record["SUPTERRCOM"]) + ' ' +
      str(record["SUPCONS"]) + ' ' +
      str(record["SUPCONSCOM"]) + ' ' +
      str(record["FRENTE"]) + ' ' +
      str(record["FONDO"]) + ' ' +
      str(float(int(record["DESNIVEL"]))) + ' ' +
      str(float(int(record["AREAINSCR"]))) + ' ' +
      str(record["UBICACION"]) + ' ' +
      str(record["NFRENTE"]) + ' ' +
      str(record["NFFONDO"]) + ' ' +
      str(record["NFIRREG"]) + ' ' +
      str(record["NFAREA"]) + ' ' +
      str(record["NFTOPOGR"]) + ' ' +
      str(record["NFUBIC"]) + ' ' +
      str(record["VALTERR"]) + ' ' +
      str(float(int(record["VALCONS"]))) + ' ' +
      str(record["ACLARACION"]) + ' ' +
      str(record["FCAPTURA"]) + ' ' +
      str(float(int(record["SUPAPROV"]))) + ' ' +
      str(record["NFSUPAPR"])







      str(record["MUNICIPIO"]) + ' ' + Numeric(3),
      str(record["ZONA"]) + ' ' + Numeric(2),
      str(record["MANZANA"]) + ' ' + Numeric(3),
      str(record["LOTE"]) + ' ' + Numeric(2),
      str(record["TIPOPREDIO"]) + ' ' + Character(1),
      str(record["REGPROP"]) + ' ' + Numeric(1),
      str(record["DOMICILIO"]) + ' ' + Character(50),
      str(record["ZONAORIG"]) + ' ' + Numeric(3),
      str(record["CODCALLE"]) + ' ' + Numeric(4),
      str(record["NUMEXT"]) + ' ' + Character(5),
      str(record["COLONIA"]) + ' ' + Character(30),
      str(record["CODPOST"]) + ' ' + Numeric(5),
      str(record["ENTCALLE"]) + ' ' + Character(21),
      str(record["YCALLE"]) + ' ' + Character(21),
      str(record["SUPTERRTOT"]) + ' ' + Numeric(10),
      str(record["SUPTERRCOM"]) + ' ' + Numeric(10),
      str(record["SUPCONS"]) + ' ' + Numeric(10),
      str(record["SUPCONSCOM"]) + ' ' + Numeric(10),
      str(record["FRENTE"]) + ' ' + Numeric(8,2),
      str(record["FONDO"]) + ' ' + Numeric(8,2),
      str(record["DESNIVEL"]) + ' ' + Numeric(6,2),
      str(record["AREAINSCR"]) + ' ' + Numeric(10),
      str(record["UBICACION"]) + ' ' + Numeric(1),
      str(record["NFRENTE"]) + ' ' + Numeric(7,5),
      str(record["NFFONDO"]) + ' ' + Numeric(7,5),
      str(record["NFIRREG"]) + ' ' + Numeric(7,5),
      str(record["NFAREA"]) + ' ' + Numeric(7,5),
      str(record["NFTOPOGR"]) + ' ' + Numeric(7,5),
      str(record["NFUBIC"]) + ' ' + Numeric(7,5),
      str(record["VALTERR"]) + ' ' + Numeric(11),
      str(record["VALCONS"]) + ' ' + Numeric(11),
      str(record["ACLARACION"]) + ' ' + Character(1),
      str(record["FCAPTURA"]) + ' ' + Date,
      str(record["SUPAPROV"]) + ' ' + Numeric(10),
      str(record["NFSUPAPR"]) + ' ' + Numeric(7,5)
"""
