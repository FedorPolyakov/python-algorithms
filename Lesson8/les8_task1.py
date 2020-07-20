# Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.
# Пример работы функции:
#
# func("papa")
# 6
# func("sova")
# 9

def func(s):
    my_set = set()
    k = 1
    while k!=len(s):
        for i in range(0,len(s)):
            if hash(s[i:i+k]) not in my_set:
                my_set.add(hash(s[i:i+k]))
        k += 1
    return f'{len(my_set)}'
s = 'sova'
print(func(s))
s = 'papa'
print(func(s))