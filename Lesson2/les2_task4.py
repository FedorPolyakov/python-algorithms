#Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.
# https://app.diagrams.net/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&page-id=2yYXt8u4D2Ydp76MgN4M&title=Lesson2Diagram.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1u_CqrRwx8lLYnRztQi1fgedMtYm90-N-%26export%3Ddownload
def task4(n):
    if n == 1:
        return 1
    return (1/((-2)**(n-1))) + task4(n-1)

n = int(input('Введите n: '))
z = task4(n)
print(z)