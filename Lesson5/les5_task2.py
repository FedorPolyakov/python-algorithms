# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как коллекция, элементы которой — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

# КОММЕНТАРИЙ:
# Успел решить только сложение
#

from collections import deque
hexdecimal = {
    '0' : 0, '1' : 1, '2' : 2, '3' : 3,
    '4' : 4, '5' : 5, '6' : 6, '7' : 7,
    '8' : 8, '9' : 9, 'A' : 10, 'B' : 11,
    'C' : 12, 'D' : 13, 'E' : 14, 'F' : 15
}
hexdecimal_ = {
    '0' : '0', '1' : '1', '2' : '2', '3' : '3',
    '4' : '4', '5' : '5', '6' : '6', '7' : '7',
    '8' : '8', '9' : '9', '10' : 'A', '11' : 'B',
    '12' : 'C', '13' : 'D', '14' : 'E', '15' : 'F'
}
a = deque(input('Введите первое число в 16-й системе счисления: '))
b = deque(input('Введите второе число в 16-й системе счисления: '))
c = deque()
final = []
a.reverse()
b.reverse()

def sum_hex(a,b):
    summa = 0
    mind = 0
    while True:
        if len(b) < len(a):
            b.append('0')
        elif len(a) < len(b):
            a.append('0')
        else:
            break
    for i in range(len(a)):
        if a[i] and b[i] in hexdecimal.keys():
            summa += hexdecimal[a[i]] + hexdecimal[b[i]]
            if mind > 0:
                summa = summa + mind
                mind = 0
            if summa >= 16:
                mind += 1
                summa = summa % 16
            c.append(str(summa))
            if i == len(a):
                c.append(str(summa))
            else:
                summa = 0
    else:
        if mind != 0:
            c.append(str(mind))
    c.reverse()
    for i in range(len(c)):
        if c[i] in hexdecimal_:
            final.append(hexdecimal_[c[i]])
    return final
print(f'Сумма двух чисел равна: {sum_hex(a,b)}')