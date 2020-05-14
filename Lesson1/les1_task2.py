# По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти точки.
# https://app.diagrams.net/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&page-id=J_h1LOgfInxqD7J5e9Ij&title=les1_diagram.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D15xNBhhB0Ye9kCCdbEjTMdzzZ1GgR_MwY%26export%3Ddownload
x1 = int(input('Введите абсциссу первой точки х1 : '))
y1 = int(input('Введите ординату первой точки у1 : '))
x2 = int(input('Введите абсциссу второй точки х2 : '))
y2 = int(input('Введите ординату второ1 точки у2 : '))
if (x1 == x2) :
    print(f'уравнение имеет вид x = {x1}')
elif (y1 == y2):
    print(f'уравнение имеет вид y = {y1}')
else:
    k = (y2-y1)/(x2-x1)
    b = y1 - k*x1
    if b >= 0 :
        print(f'y={k}x+{b}')
    else:
        print(f'y={k}x{b}')
