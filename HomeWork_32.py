# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

# первый вариант

# def get_indexes(arr, min_val, max_val):
#     indexes = []
#     for i in range(len(arr)):
#         if min_val <= arr[i] <= max_val:
#             indexes.append(i)
#     return indexes

# arr = [1, 5, 10, 15, 20]
# min_val = 5
# max_val = 15

# indexes = get_indexes(arr, min_val, max_val)
# print(f"Индексы элементов массива, значения которых принадлежат диапазону [{min_val}, {max_val}]:")
# print(indexes)

# второй вариант

import random

def get_indexes(arr, min_val, max_val):
    indexes = []
    for i in range(len(arr)):
        if min_val <= arr[i] <= max_val:
            indexes.append(i)
    return indexes

# Создаем массив заполненный случайными значениями
arr = [random.randint(0, 100) for _ in range(10)]
min_val = 25
max_val = 75

indexes = get_indexes(arr, min_val, max_val)
print(f"Массив: {arr}")
print(f"Диапазон поиска: [{min_val}, {max_val}]")
print(f"Индексы элементов массива, значения которых принадлежат диапазону:")
print(indexes)