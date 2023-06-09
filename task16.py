# Задача 16: Требуется вычислить, сколько раз встречается
# некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число
# N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X

# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

from random import randint

number = int(input('Введите число элементов: '))
array = []
for i in range(number):
    array.append(randint(1, 10))
print(array)
find_number = int(input('Введите число X: '))
count = 0
for i in range(number):
    if array[i] == find_number:
        count += 1
print(f'Число {find_number} встречается {count} раз')