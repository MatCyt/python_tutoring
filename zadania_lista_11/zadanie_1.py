# Napisz funkcje, która rekurencje będzię sie wywoływała aby wyświetlać zawartość folderu. 
# Folder czyli tak naprawde jego scieżka ma byc przekazywana jako parametr funkcji.

import os

path = 'c:\\Users\\mcytrowski\\Desktop\\python_tutoring'

def show_directory_content(path):
    for item in os.listdir(path):
        # new_path = "{}\{}".format(path,file)
        print(item)
        new_path = "{}\{}".format(path,item)
        show_directory_content(item)

show_directory_content(path)


# PRZYKŁADOWE ROZWIĄZANIE
def list_directory_content(path):
    path = os.path.abspath(path)
    for file in os.listdir(path):
        file_absolute_path = "{}\{}".format(path,file)
        print(file_absolute_path)
        if os.path.isdir(file_absolute_path):
            list_directory_content(file_absolute_path)

list_directory_content("./")