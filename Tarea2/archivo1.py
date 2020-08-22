import json

def readJson():
    miArchivo = open('archivo1.json')
    data = json.load(miArchivo)
    miArchivo.close()
    print(data)
    return data

dict=readJson()
for palabras in dict:
    print(palabras)
print('Tipo de la estructura',type(readJson))


