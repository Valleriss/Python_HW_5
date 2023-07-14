
# # 1.Создайте список из случайных чисел. Найдите номер его последнего локального максимума.
# #  Локальный максимум - элемент, который больше любого из своей соседей.

import random
n = int(input('Введите количество элементов: '))
list = [random.randint(-50, 50) for item in range(n)]
print(list)
local_max = 0
for i in range(1, len(list) - 1):
    if list[i] > list[i - 1] and list[i] > list[i + 1]:
        local_max = list[i]
print(local_max)
print(i)

#2.Создайте список из случайных чисел. Найдите максимальное количество его одинаковых элементов.
import random 
n = int(input('Введите количество элементов: '))
numbers = [random.randint(1, 10) for _ in range(n)] 
count_dict = {} 
for num in numbers: 
    if num in count_dict: 
        count_dict[num] += 1 
    else: 
        count_dict[num] = 1 
max_count = max(count_dict.values()) 
print(numbers)
print("Максимальное количество одинаковых элементов:", max_count)


# # 3.Создайте список из случайных чисел. Найдите второй максимум.
# a = [1, 2, 3] # Первый максимум == 3, второй == 2
import random
n = int(input('Введите количество элементов: '))
list = [random.randint(-50, 50) for item in range(n)]
print(list)
list.sort()
print(list[-2])


# 4.Создайте список из случайных чисел. Найдите количество различных элементов в нем.

import random 
n = int(input('Введите количество элементов: '))
numbers = [random.randint(1, 10) for _ in range(n)]
keys = [] 
for i in range(n):
    if numbers[i] not in keys:
        keys.append(numbers[i])
print(numbers)
print(len(keys))

