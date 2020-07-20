# Написать два алгоритма нахождения i-го по счёту простого числа.
#  Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
#  Проанализировать скорость и сложность алгоритмов.
#
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
#  Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
import timeit
import cProfile

def f_sieve(number):
    t = number
    n = 1000
    while True:
        sieve = [i for i in range(n)]  # квадратные скобки (массив) в рамках алгоритма, но не для использования в ПЗ
        # print(sieve)
        sieve[1] = 0

        for i in range(2, n):
            if sieve[i] != 0:
                j = i + i
                while j < n:
                    sieve[j] = 0
                    j += i
        # print(sieve)
        res = [i for i in sieve if i != 0]
        # return f'{len(res)}'
        if t > len(res):
             n += 1000
        else:
             return f'решето {res[t - 1]}'


# Второй — без использования «Решета Эратосфена».
def prime(m):
    def issimple(n):
        for i in range(2,int(n**(0.5))+1):
            if n % i == 0:
                return False
        return True
    n=5
    s=[2,3]
    k = m
    if k == 1:
        return s[0]
    elif k == 2:
        return s[1]
    while True:
        if issimple(n) is True:
            s.append(n)
        if len(s) == k :
            break
        n+=2
    return f'не решето {s[-1]}'

number = int(input('Введите номер простого числа: '))
print(prime(number))
print(f_sieve(number))

print(timeit.timeit('prime(10)', number=10000, globals=globals()))#   0.1274876
print(timeit.timeit('prime(100)', number=10000, globals=globals()))#  2.7234149
print(timeit.timeit('prime(1000)', number=10000, globals=globals()))# 65.23655310000001
print('-'*100)
print(timeit.timeit('f_sieve(10)', number=10000, globals=globals()))#   2.4738109999999978
print(timeit.timeit('f_sieve(100)', number=10000, globals=globals()))#  3.361986299999998
print(timeit.timeit('f_sieve(1000)', number=10000, globals=globals()))# 112.01937730000002


cProfile.run('prime(100)')  # 1    0.000    0.000    0.000    0.000 les4_task2.py:35(prime)
                            # 269    0.000    0.000    0.000    0.000 les4_task2.py:36(issimple)
cProfile.run('prime(1000)') # 1    0.001    0.001    0.007    0.007 les4_task2.py:35(prime)
                            # 3958    0.005    0.000    0.005    0.000 les4_task2.py:36(issimple)
cProfile.run('prime(10000)')# 1    0.014    0.014    0.148    0.148 les4_task2.py:35(prime)
                            # 52363    0.131    0.000    0.131    0.000 les4_task2.py:36(issimple)
print('-'*100)
cProfile.run('f_sieve(100)')  # 1    0.000    0.000    0.000    0.000 les4_task2.py:11(f_sieve)
cProfile.run('f_sieve(1000)') # 1    0.007    0.007    0.009    0.009 les4_task2.py:11(f_sieve)
cProfile.run('f_sieve(10000)')# 1    1.614    1.614    1.924    1.924 les4_task2.py:11(f_sieve)

############################################################
## КОММЕНТАРИИ: по идее решето Эратосфена быстрый способ посчитать простое число, по сравнению
# с обычным перебором проверки числа на простоту(где идет проверка от 2 до n), однако
# чтобы проверить является ли число простым, достаточно проверить корень из n значений - такая вот оптимизация.
# Так же для усовешенствования алгоритма решета был введен дополнительный цикл для увеличеня размера решета,
# поэтому ф-я решения через решето похоже имеет кубическую ассимптотику ( 3 вложенных цикла),
# а алгоритм решения без решета - квадратичную ( 2 вложенных цикла)
############################################################
