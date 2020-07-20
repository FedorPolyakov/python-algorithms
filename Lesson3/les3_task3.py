# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

SIZE = 20
MIN_ITEM = 0
MAX_ITEM = 10000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

MIN_EL = 0
MAX_EL = 0
for i in range(len(array)):
    if array[i] > array[MAX_EL]:
        MAX_EL = i
    if array[i] < array[MIN_EL]:
        MIN_EL = i
else:
    array[MIN_EL] = array[MIN_EL] + array[MAX_EL]
    array[MAX_EL] = array[MIN_EL] - array[MAX_EL]
    array[MIN_EL] = array[MIN_EL] - array[MAX_EL]

print(array)