import xml.etree.ElementTree as ET
archivo_xml = ET.parse('archivo3.xml')

raiz = archivo_xml.getroot()


 

for hijo in raiz:
    print(hijo.tag, hijo.attrib)

print('Tipo de la estructura',type(hijo))