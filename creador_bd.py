#!/usr/bin/python
import psycopg2
    # PARA COMANDOS EN GENERAL
conn = psycopg2.connect("host=localhost port=5432 dbname=estadodemexico user=postgres password='12345'")
cur = conn.cursor()
#linea ejecutora de comandos sql de postgresql
#sqlcommand_createdb = "CREATE database estadodemexico"
#print("base datos creada")
"""
cadenaschema = ""
for num in range(1, 126):
    #print("mun" + str(num).zfill(3))
    cadenaschema = "mun" + str(num).zfill(3)

    sqlcommand_createdb = "CREATE  SCHEMA " + cadenaschema +" AUTHORIZATION postgres;"
    cur.execute(sqlcommand_createdb)
    conn.commit()

print("esquemas cargados")
conn.close()
"""
