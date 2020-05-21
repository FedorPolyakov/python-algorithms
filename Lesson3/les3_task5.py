#В массиве найти максимальный отрицательный элемент.
#  Вывести на экран его значение и позицию в массиве.
#  Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
#  Это два абсолютно разных значения.
import random

SIZE = 20
MIN_ITEM = -20
MAX_ITEM = 5
array = [random.randint(MIN_ITEM,MAX_ITEM) for _ in range(SIZE)]
MIN_ID = -1

for i in range(len(array)):
    if array[i] < 0:
        MIN_ID = i
    elif (array[i] < 0 and array[i] >= MIN_EL):
        MIN_ID = i

print(array)
print(f'максимальный отрицательный элемент {array[MIN_ID]} номер последнего такого элемента {MIN_ID}')