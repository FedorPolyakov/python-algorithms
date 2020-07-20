# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
#  Найдите в массиве медиану. Медианой называется элемент ряда,
#  делящий его на две равные части: в одной находятся элементы, которые не меньше медианы,
#  в другой — не больше медианы.

# Примечание: задачу можно решить без сортировки исходного массива.
#  Но если это слишком сложно, используйте метод сортировки,
#  который не рассматривался на уроках (сортировка слиянием также недопустима).
import random
import timeit

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(2*SIZE+1)]
# массив для проверки, с несколькими повторяющимеся элементами
# array = [-100, 100, 100, 100, 3, 4, 4, 0, 0, 4, 4, 4, -33, -33, -7]

def find_median(mas):
    for i in range(len(mas)):
        n = m = k = 0 #переменные для значений меньше(n), больше(m) и равного(k) i-го(-му) элементу
        for j in range(len(mas)):
            if mas[j] != mas[i]:
                if mas[j] > mas[i]:
                    n += 1
                else:
                    m += 1
            if mas[j] == mas[i]:
                k += 1
        if n == m:
            return mas[i]
        elif n - m in range(1,k):
            return mas[i]
        elif m - n in range(1,k):
            return mas[i]

#просто функция для проверки
def check_sort(mas):
    mas = sorted(mas)
    return mas[len(mas)//2]

print(f'Исходный массив:\n{array}')
print(f'Медиана без сортировки массива: {find_median(array)}')
print('-'*100)
print(f'Отсортируем массив функцией sorted для проверки\n{sorted(array)}')
print(f'Медиана отсортированного масива: {check_sort(array)}')
# Посмотрим что лучше по времени выполнения
# Спойлер - функция сортировки sorted будет быстрее примерно на 2 порядка
print('-'*100)
print(timeit.timeit('find_median(array)', number=1000, globals=globals())) #0.06924749999999999
print(timeit.timeit('check_sort(array)', number=1000, globals=globals()))  #0.0007469999999999977