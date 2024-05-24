#!/usr/bin/python
import psycopg2
import csv
# PARA CONSULTAS
#https://www.dataquest.io/blog/loading-data-into-postgres/
#https://docs.python.org/es/3.9/library/csv.html
print("leer csv header para solo columnas construcciones x municipio")

headercsv = ""
sqlcommand = ""
for num in range(1, 126):
    print("m" + str(num).zfill(3))
    cadenaschema = "m" + str(num).zfill(3)
    print(cadenaschema)
    cadenaschema_base_datos = "mun" + str(num).zfill(3)
    print(cadenaschema_base_datos)
    with open( cadenaschema + '/construcciones.csv', newline='', encoding='latin_1') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            headercsv ='drop table IF EXISTS ' + cadenaschema_base_datos + '.construcciones CASCADE; create table ' + cadenaschema_base_datos + '.construcciones ('+ ' text, '.join(row).lower()+ ' text );'
            sqlcommand ='insert into '+ cadenaschema_base_datos +'.construcciones ('+ ' , '.join(row).lower()+ '  ) VALUES ( '
            sqlvalues ='|'.join(row).lower()+ '|'
            valorresultante = sqlvalues.count('|')
            mensaje2a = '%s,' * int(valorresultante)
            cadenavg = mensaje2a
            buggy_name = cadenavg
            cadenalista = buggy_name[:-1]
            cadenalista2 = cadenalista + ' )'
            #print( sqlcommand + cadenalista2)
            sqlcommand_exe = sqlcommand + cadenalista2
            break
    # PARA COMANDOS EN GENERAL
    conn = psycopg2.connect("host=localhost port=5432 dbname=estadodemexico user=postgres password='12345'")
    cur = conn.cursor()
    #linea ejecutora de comandos sql de postgresql
    headercsv2 = headercsv;
    cur.execute(headercsv2)
    conn.commit()
    print("TABLAS DE CONSTRUCCIONES CREADAS EXITO")
    conn.close()
