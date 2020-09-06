
cadena = '_a3'
cadenaaa = '_servidor3'
cadena3 = '_servidor'

def AFD(entrada):
    estado=0
    for letra in range(len(entrada)):
        if estado == 0:
            if entrada[letra] == '_':
                estado = 1
            else:
                print("Cadena incorrecta")
                return
        elif estado == 1:
            if entrada[letra] == str(letra).isalpha() or str(letra).isdigit():
                estado = 2
            else:
                print("Cadena incorrecta")
                return
        elif estado == 2:
            if entrada[letra] == str(letra).isdigit():
                estado = 3
            else:
                print("Cadena incorrecta")
                return
    if estado == 3:
        print('Cadena bueba')
   
AFD(cadena)







    