# Write a script comparing the content of two txt files (student names) and printing back only shared values (names)

import numpy as np

def read_txt(file_name):
    with open(file_name, "r") as f:
        test = f.read()
        return test.split('\n')


studenci_python = read_txt('studenci_python.txt')
studenci_cpp = read_txt('studenci_cpp.txt')

# all
shared = [name for name in studenci_python if name in studenci_cpp]

# unique
studenci_python_u = np.unique(studenci_python)
studenci_cpp_u = np.unique(studenci_cpp)
shared_unique = [name for name in studenci_python_u if name in studenci_cpp_u]

# by hand
shared_students = []
for student in studenci_python:
    if student in studenci_cpp and student not in shared_students:
        shared_students.append(student)

# rozwiązanie z teorii 9
studenci_python.intersection(studenci_cpp)

# Internet found solution
internet_solution = set(studenci_python) & set(studenci_cpp)
# print(len(internet_solution))



