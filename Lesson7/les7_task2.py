# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 49
array = [(random.randint(MIN_ITEM, MAX_ITEM) + random.randint(1,9)/10) for _ in range(SIZE)]

def merge_sort(mas):
    # print(mas)
    if len(mas) > 1:
        middle = len(mas)//2
        left = mas[:middle]
        right = mas[middle:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                mas[k] = left[i]
                i += 1
            else:
                mas[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            mas[k] = left[i]
            i+=1
            k+=1

        while j < len(right):
            mas[k] = right[j]
            j+=1
            k+=1
    return mas

print(f'Исходный массив:\n{array}')
print(f'Отсортированный массив методом слияния:\n{merge_sort(array)}')