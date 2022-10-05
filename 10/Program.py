# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:для k = 8 список: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

number = int(input("Введите число: "))

def Fibonacci(number):
        if number < 0:
            return Fibonacci(abs(number)) * (-1)**(number + 1)
        if number == 0:
            return 0
        if number == 1:
            return 1
        else:
            return Fibonacci(number - 1) + Fibonacci(number - 2)

for i in range (-number, number + 1):
    print(Fibonacci(i))