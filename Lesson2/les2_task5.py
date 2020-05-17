# Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел
# выполняется равенство: 1+2+...+n = n(n+1)/2, где n — любое натуральное число.
# https://app.diagrams.net/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&page-id=8VDDnpGlRYquR-yhwQ6C&title=Lesson2Diagram.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1u_CqrRwx8lLYnRztQi1fgedMtYm90-N-%26export%3Ddownload
def task5(n):
    if n == 1:
        return 1
    return n + task5(n-1)

n  = int(input('Введите n: '))
leftsum = task5(n)
rightsum = n*(n+1)/2
print(f'Левая часть равенства равна : {leftsum}')
print(f'Правая часть равенства равна : {rightsum}')
if leftsum == rightsum:
    print('Равенство выполняется')
else:
    print('Равенство невыполняется')