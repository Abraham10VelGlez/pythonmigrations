#!/usr/bin/python
import psycopg2
import csv
# PARA CONSULTAS
#https://www.dataquest.io/blog/loading-data-into-postgres/
#https://docs.python.org/es/3.9/library/csv.html
print("leer csv header para solo columnas de cada archivo")
headercsv = ""
sqlcommand = ""
with open('predios.csv', newline='', encoding='latin_1') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        #creas la tabla que contenga los datos
        headercsv ='drop table IF EXISTS mun01.predios CASCADE; create table mun01.predios ('+ ' text, '.join(row).lower()+ ' text );'
        sqlcommand ='insert into mun01.predios ('+ ' , '.join(row).lower()+ '  ) VALUES ( '
        sqlvalues ='|'.join(row).lower()+ '|'
        #print(sqlvalues.count('|'))
        valorresultante = sqlvalues.count('|')
        #print(valorresultante)
        mensaje2a = '%s,' * int(valorresultante)
        cadenavg = mensaje2a
        #print(cadenavg)
        buggy_name = cadenavg
        cadenalista = buggy_name[:-1]
        #print(cadenalista)
        cadenalista2 = cadenalista + ' )'
        #print(cadenalista2)

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
print("TABLA CREADA EXITO")
conn.close()
# PARA COMANDOS DE IMPORTACION DE CSV A POSTGRESQL
class load_avg:

    def load_excel(avg):
        avg.archivo = open (r"predios.csv")
        avg.filas = csv.reader( avg.archivo, delimiter = ",")
        avg.lista = list(avg.filas)
        # Eliminación del primer registro por que es la cabecera del archivo
        del (avg.lista[0])
        avg.tupla = tuple(avg.lista)
        for rw in avg.tupla:
            #print(rw)
            rw
            #break


    def load_to_bd(avg):
        avg.connection = psycopg2.connect("host=localhost port=5432 dbname=estadodemexico user=postgres password='12345'")
        avg.cur = avg.connection.cursor()
        avg.cur.execute("truncate mun01.predios;");
        avg.connection.commit()
        sqlcommand3 = sqlcommand_exe
        #print(str(sqlcommand3))
        #avg.cur.executemany("insert into arbol.nombretabla (municipio , areahom , descareaho , uso , clasif , valm2suelo , aniovigvus , frentebase , fondobase , fechacap , movimi , observa  ) VALUES ( %s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s,%s ,%s )",avg.tupla)
        avg.cur.executemany(sqlcommand3,avg.tupla)
        avg.connection.commit()
        avg.connection.close()






load_avg2 = load_avg()
load_avg2.load_excel()
load_avg2.load_to_bd()
print("INSERTACION COMPLETA STUDIO A")
