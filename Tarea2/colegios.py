import csv

with open('colegios.csv', newline='') as File:
    lectura = csv.reader(File)
    for columna in lectura:
        print(columna)
print('Tipo de la estructura',type(lectura))