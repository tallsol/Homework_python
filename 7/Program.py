# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16];

array = [2, 3, 4, 5, 6]
new_array = []
last_pos = len(array) - 1

for i in range(len(array)):
    if i <= last_pos:
        new_array.append(array[i] * array[last_pos])
        last_pos -= 1

print (new_array)