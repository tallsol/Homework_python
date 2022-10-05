# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:[1.1, 1.2, 3.1, 5, 10.01] => 0.19

from fractions import Fraction


array = [1.1, 1.2, 3.1, 5, 10.01]

def find_min (array):
    min = 1
    for i in array:
        if i % 1 < min:
            min = i % 1
    return min

def find_max (array):
    max = 0
    for i in array:
        if i % 1 > max:
            max = i % 1
    return max

max = (find_max(array))
min = (find_min(array))

print(max-min)