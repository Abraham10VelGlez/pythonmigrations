#!/usr/bin/python
import csv
from dbfread import DBF

print("Iniciando convertidor")
# ciclo x municipio
    #print("CONVERSION FINALIZADA DEL MUNICIPIO " + str(num).zfill(3) )
#!/usr/bin/python
print("calculos")
for num in range(1, 126):
    if num == 9 or num == 24  or num == 30  or num == 86 or num == 118  or num == 125 :
        #print(str(num).zfill(3) + " Muninicio con detalles a resolver en linux")
        print("CONVERSION DETENIDA, CONTIENE ERRORES DE PREDIOS NIVEL ESTADO DE MEXICO MUNICIPIO " + str(num).zfill(3) )
        continue
    else:
        #print(str(num).zfill(3) + " Muninicio migrado con exito" )
        numeroconceros = str(num).zfill(3)
        municipiocadenaconnumeros = "m" + numeroconceros
        #print(municipiocadenaconnumeros)
        #def dbf_to_csv_to_predios(path):
        #print(municipiocadenaconnumeros+'/GC203T04.dbf')
        path=str(municipiocadenaconnumeros+'/GC203T04.dbf')
        #print(path)
        # Set the name of the CSV file
        print("CARGANDO CONVERSION DE PREDIOS NIVEL ESTADO DE MEXICO MUNICIPIO " + str(num).zfill(3) )
        csv_path = municipiocadenaconnumeros + "/predios.csv"
        print(csv_path)
        dbf = DBF(path,encoding='latin_1')
        with open(csv_path, 'w', newline = '',encoding="latin_1") as f:
            writer = csv.writer(f)
            writer.writerow(dbf.field_names)
            for record in dbf:
                #muestra los datos en forma de lista
                writer.writerow(list(record.values()))
                csv_path
