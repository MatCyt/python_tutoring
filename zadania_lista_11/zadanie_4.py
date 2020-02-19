# Napisz skrypt, który wczyta przykładowy plik json i wypisze wszystkie w nim zawarte nazwy Państw.

import json

with open('./zadania_lista_11/kraje.json') as f:
    data = json.load(f)

for i in data['products']:
    print(i['name'])