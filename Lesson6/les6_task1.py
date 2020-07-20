# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

#Задача №4 урока №3
# Определить, какое число в массиве встречается чаще всего.

# КОММЕНТАРИЙ:
# Возможно, я выбрал слишком простую задачу, или же не понял задания.
# так же я воспользовался модулем memory_profiler.
# Этот модуль добавляет декоратор @profile, позволяющий отслеживать какое-то конкретное применение памяти.
# Наверное это не правильно.. но по другому я не смог придумать как автоматизовать подсчет памяти
# На моем компьютере (Win10 x64) память тратилась везде одинаково(опять же, если я все правильно сделал..)
# Поэтому какой способ лучше по памяти судить сложно.
# Сумма по памяти составила 16.5 Миб.



import random
from collections import Counter
from memory_profiler import profile


SIZE = 1000
MIN_ITEM = -10
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

@profile
def var_1(array):
    num = array[0]
    frequency = 1
    for i in range(len(array)):
        spam = 1
        for j in range(i + 1, len(array)):
            if array[i] == array[j]:
                spam += 1
        if spam > frequency:
            frequency = spam
            num = array[i]
    return num

@profile
def var_2(array):
    counter = {}
    frequency = 1
    num = None
    for item in array:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1

        if counter[item] > frequency:
            frequency = counter[item]
            num = item
    return num

@profile
def var_3(array):
    frequency = 1
    id = -1
    dct = Counter(array)
    for key, value in dct.items():
        if value > frequency:
            frequency = value
            id = key
    return id


if __name__ == "__main__":
    var_1(array)
    var_2(array)
    var_3(array)