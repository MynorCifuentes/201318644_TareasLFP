import json
import webbrowser


def readJson():
    miArchivo = open('Tarea4.json')
    data = json.load(miArchivo)
    miArchivo.close()
    #print(data)
    return data

lista = list()
dict = readJson()
mensajeArriba ="""
<html>
    <head></head>
    <body>
    <table>
"""
mensajeAbajo="""
</table>
    </body>
    </html>
    """
mensaje=""
for palabras in dict:
    print(palabras)
    mensaje += """
    
    <tr>
    <td>"""+ palabras+ """"</td>
    </tr>
    """
   
#print(lista)
     
 


f = open('Tarea4.html', 'wb')

# for()
# mensaje= """<html>
# <head></head>
# <body>
# <tr>

#     <td>Cell 1</td>

#     <td>Cell 2</td>

#     <td>Cell 3</td>

#   </tr>

#   <tr>

#     <td>Cell 4</td>

#     <td>Cell 5</td>

#     <td>Cell 6</td>

#   </tr>

# </table>
# <p>"""+str(lista)+"""</p></body>
# </html>"""
mensajes = mensajeArriba+mensaje+mensajeAbajo
bytes = mensajes.encode(encoding='UTF-8')

f.write(bytes)
f.close()

webbrowser.open_new_tab('Tarea4.html')
