# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал
# (т.е. 4 числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести
# наименования предприятий, чья прибыль выше среднего и ниже среднего.
from collections import  Counter
QUARTER = 4
k = 1
profit = 0
avg_profit = 0

while True:
    n = int(input('Введите количество предприятий: '))
    if n > 0:
        break

factory = Counter({})
while k != n+1:
    i = input(f'Введите название {k}-го предприятия: ')
    for j in range(QUARTER):
        profit += int(input(f'Введите название для предприятия {i} за {j+1}-й квартал: '))
    factory[i] = profit
    avg_profit += profit
    profit = 0
    k += 1
else:
    print(f'Средняя прибыль для всех предприятий составила: {avg_profit/n}')
    print(f'Предприятия с прибылью меньше средней: {[key for key,value in factory.items() if value < avg_profit/n]}')
    print(f'Предприятия с прибылью больше средней: {[key for key,value in factory.items() if value > avg_profit/n]}')
