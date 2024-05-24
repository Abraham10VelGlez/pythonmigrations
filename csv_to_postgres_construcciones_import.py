#!/usr/bin/python
import psycopg2
import csv
cadenaschema = ""
for num in range(1, 126):
    #print("mun" + str(num).zfill(3))
    cadenasfilescarpt = "m" + str(num).zfill(3)
    cadenaschemasql = "mun" + str(num).zfill(3)



    headercsv = ""
    sqlcommand = ""
    with open( cadenasfilescarpt + '/construcciones.csv', newline='', encoding='latin_1') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            #creas la tabla que contenga los datos
            headercsv ='drop table IF EXISTS '+ cadenaschemasql +'.construcciones CASCADE; create table '+ cadenaschemasql +'.predios ('+ ' text, '.join(row).lower()+ ' text );'
            sqlcommand ='insert into ' + cadenaschemasql + '.construcciones ('+ ' , '.join(row).lower()+ '  ) VALUES ( '
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

    # PARA COMANDOS DE IMPORTACION DE CSV A POSTGRESQL
    class load_avg:

        def load_excel(avg):
            cadena_resultante = cadenasfilescarpt +'/construcciones.csv'
            #print(cadena_resultante)
            avg.archivo = open (r""+cadena_resultante+"", newline='', encoding='latin_1')
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
            avg.cur.execute("truncate " +cadenaschemasql+ ".construcciones;");
            avg.connection.commit()
            sqlcommand3 = sqlcommand_exe
            #print(str(sqlcommand3))
            #avg.cur.executemany("insert into arbol.nombretabla (municipio , areahom , descareaho , uso , clasif , valm2suelo , aniovigvus , frentebase , fondobase , fechacap , movimi , observa  ) VALUES ( %s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s,%s ,%s )",avg.tupla)
            avg.cur.executemany(sqlcommand3,avg.tupla)
            avg.connection.commit()
            print("TABLA construcciones DEL MUNICIPIO "+ str(num).zfill(3) +" CARGADA A POSTGRESQL ")
            avg.connection.close()






    load_avg2 = load_avg()
    load_avg2.load_excel()
    load_avg2.load_to_bd()
    print("INSERTACION COMPLETA STUDIO A")
