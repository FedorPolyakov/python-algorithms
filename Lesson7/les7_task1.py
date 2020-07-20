# Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).

# КОММЕНТАРИЙ:
# Как можно улучшить сортировку пузырьком? см статью на вики: сортировка пузырьком
import random
import timeit

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
# array = [-38, -69, 76, -27, 90, -39, -11, 15, -31, -28]

#улучшенная сортировка пузырьком
def bubble_sort_1(mas):
    n = 1
    while n < len(mas):
        flag = 0
        for i in range(len(mas)-1):
            if mas[i+1] > mas[i]:
                mas[i+1],mas[i] = mas[i],mas[i+1]
                flag = 1
        if flag == 0:
            break
        n += 1
    return mas

#обычная сортировка пузырьком
def bubble_sort_2(mas):
    for j in range(len(mas)):
        for i in range(len(mas)-j-1):
            if mas[i] < mas[i+1]:
                mas[i], mas[i+1] = mas[i+1], mas[i]
    return mas

print(f'Исходный массив:\n{array}')
print(f'Отсортированный по убыванию массив:\n{bubble_sort_1(array)}')
print('-'*100)
#Сравним время сортировки пузырьком улучшенного метода и обычного
#путем улучшения метода можно улучшить время сортировки примерно в раз
print(timeit.timeit('bubble_sort_1(array)', number=1000, globals=globals())) #0.0010102999999999987
print(timeit.timeit('bubble_sort_2(array)', number=1000, globals=globals())) #0.005910600000000002