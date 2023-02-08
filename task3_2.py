# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

from random import randint
n = int(input("Введите длину массива: "))
arr=[randint(1,10) for i in range(n)]
print(arr)
x = int(input("Введите число: "))

minDif = abs(arr[0] - x)
num = arr[0]
for i in range(1, len(arr)):
    if abs(x - arr[i]) < minDif:
        minDif = abs(arr[i] - x)
        num = arr[i]
print(num)