# Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.
# N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

from math import factorial

number = int(input("Input number: "))

i = 1
list = []

while i <= number:
    list.append(factorial(i))
    i += 1

print(list)
