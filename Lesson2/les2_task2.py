# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
# https://app.diagrams.net/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&page-id=JzzySUl43xAIpPyjjLHP&title=Lesson2Diagram.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1u_CqrRwx8lLYnRztQi1fgedMtYm90-N-%26export%3Ddownload
def task2(x):
    numeven = 0
    numodd = 0
    even = ''
    odd = ''
    for i in x:
        if int(i) % 2 == 0:
            numeven += 1
            even += i+' '
        else:
            numodd += 1
            odd += i+' '
    return f'количество четных цифр: {numeven}, цифры:{even}; количество нечентных цифр: {numodd}, цифры:{odd}'

x = input('Введите число большее нуля: ')
z = task2(x)
print(z)
