#По длинам трех отрезков, введенных пользователем,
# определить возможность существования треугольника, составленного из этих отрезков.
# Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным или равносторонним.
# https://app.diagrams.net/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&page-id=z6ycxpM9CIgQiqPbdBox&title=les1_diagram.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D15xNBhhB0Ye9kCCdbEjTMdzzZ1GgR_MwY%26export%3Ddownload
a = float(input('Введите первый длину первого отрезка : '))
b = float(input('Введите первый длину второго отрезка : '))
c = float(input('Введите первый длину третьего отрезка : '))

if a < b + c:
    if b < a + c:
        if c < a + b:
            if ((a == b) and (a == c) and (b == c)):
                print('Треугольник равносторонний')
            elif ((a == b) or (a == c) or (b == c)):
                print('Треугольник равнобедренный')
            else:
                print('Треугольник разносторонний')
        else:
            print('Треугольник не существует')
    else:
        print('Треугольник не существует')
else:
    print('Треугольник не существует')
