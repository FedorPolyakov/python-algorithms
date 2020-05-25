#задача №4 урока 2
# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.
import timeit
import cProfile

#вариант с циклом
def loop(n):
    item = 1
    sum_1 = 0
    for _ in range(n):
        sum_1 += item
        item /= -2      # item *= -0.5
    return sum_1

# вариант с геометрической прогрессией
def progr(n):
    sum_2 = 1 * (1 - (-0.5) ** n) / (1 - (-0.5))
    return sum_2
# вариант с рекурисей
def recur(n):
    if n == 1:
        return 1
    return 1/((-2)**(n-1)) + recur(n-1)

print(timeit.timeit('loop(5)', number=1000, globals=globals())) #0.0017079000000000018
print(timeit.timeit('geom_progr(5)', number=1000, globals=globals())) #0.00032220000000000165
print(timeit.timeit('recur(5)', number=1000, globals=globals())) #0.0018891000000000047
print('-'*50)
print(timeit.timeit('loop(50)', number=1000, globals=globals())) #0.006060900000000001
print(timeit.timeit('geom_progr(50)', number=1000, globals=globals())) #0.00030639999999999834
print(timeit.timeit('recur(50)', number=1000, globals=globals())) #0.0316837
print('-'*50)
print(timeit.timeit('loop(500)', number=1000, globals=globals())) #0.05678910000000001
print(timeit.timeit('geom_progr(500)', number=1000, globals=globals())) #0.00030520000000000547
print(timeit.timeit('recur(500)', number=1000, globals=globals())) #0.5176824
print('-'*50)
print(timeit.timeit('loop(900)', number=1000, globals=globals())) #0.06388210000000005
print(timeit.timeit('geom_progr(900)', number=1000, globals=globals())) #0.00030649999999998734
print(timeit.timeit('recur(900)', number=1000, globals=globals())) #1.0445829
# print('-'*100)
cProfile.run('loop(5)')  # 1    0.000    0.000    0.000    0.000 les4_task1.py:8(loop)
cProfile.run('loop(50)') # 1    0.000    0.000    0.000    0.000 les4_task1.py:8(loop)
cProfile.run('loop(500)')# 1    0.000    0.000    0.000    0.000 les4_task1.py:8(loop)
cProfile.run('loop(900)')# 1    0.000    0.000    0.000    0.000 les4_task1.py:8(loop)
print('-'*100)
cProfile.run('progr(5)')  # 1    0.000    0.000    0.000    0.000 les4_task1.py:17(progr)
cProfile.run('progr(50)') # 1    0.000    0.000    0.000    0.000 les4_task1.py:17(progr)
cProfile.run('progr(500)')# 1    0.000    0.000    0.000    0.000 les4_task1.py:17(progr)
cProfile.run('progr(900)')# 1    0.000    0.000    0.000    0.000 les4_task1.py:17(progr)
print('-'*100)
cProfile.run('recur(5)')  # 5/1    0.000    0.000    0.000    0.000 les4_task1.py:21(recur)
cProfile.run('recur(50)') # 50/1    0.000    0.000    0.000    0.000 les4_task1.py:21(recur)
cProfile.run('recur(500)')# 500/1    0.001    0.000    0.001    0.001 les4_task1.py:21(recur)
cProfile.run('recur(900)')# 900/1    0.001    0.000    0.001    0.001 les4_task1.py:21(recur)

################################################
## комментарии: алгоритм нахождения суммы ряда через геометрическую погрешность
# имеет наименьшую трудоемкость по времени - O(const), т.е. не зависит от размера входных данных
# алгоритмы нахождения суммы ряда через цикл и рекурсю имеют линейную трудоемкость по временеи - O(n).
# однако алгоритм рекурсии чуть медленнее и не позволяет получать результат для больших входных даннх - есть ограничения
# по стеку вызова рекурсий (который можно обойти, но лучше не надо).
# Другими словами, если линейны алгоритм записать в виде уравения прямой y = kx + b
# то, алгоритм через цикл имеет более низккий коэффициент k по сравнению с алгоритмом через рекурсию, следовательно
# алгоритм с использованием цикла лучше рекурсивного. Но самый лучший алгоритм - формула геометрической прогрессии
#################################################

