# Napisz skrypt, który wczyta przykładowy plik xml i wypisze wszystkie w nim zawarte nazwy Państw

import xml.etree.ElementTree as ET 

xml_file = ET.parse('./zadania_lista_11/kraje.xml')

root = xml_file.getroot()

for child in root:
    print(child.attrib)

for country in root.findall('country'):
    country_name = country.get('name')
    print(country_name)