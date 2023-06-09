# Задача 18: Требуется найти в массиве A[1..N]
# самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число
# N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X.
# Если таких значений больше одного, вывести первый найденный.

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5


# N = abs(int(input('Введите количество элементов списка А: ')))
# array = []
# for i in range(N):
#     array.append(randint(1, 100))
# print(array)

# A_num = list(map(int, array))
# if len(A_num) != N or N == 0:
#     print('Введенные элементы не соответствуют заявленному количеству!')
# else:
#     X = int(input('Введите число X, с которым необходимо сравнивать элементы списка: '))
#     min = abs(X - A_num[0])
#     index = 0
#     for i in range(1, N):
#         count = abs(X - A_num[i])
#         if count < min:
#             min = count
#             index = i
#     print(f'Число {A_num[index]} в списке A наиболее близко по величине к числу {X}, их разница составляет {abs(X - A_num[index])}')

from random import randint
len_nums = int(input('Enter list length: '))
nums = [randint(1, 100) for i in range(len_nums)]
print("List: ", *nums)
x = int(input('Enter x: '))
min_diff = nums[0]
for i in nums:
    diff_current = abs(i-x)
    if diff_current < min_diff:
        res = i
        min_diff = diff_current
res = min([i for i in nums if abs(i-x) == min_diff])
print(f'Result is {res}')