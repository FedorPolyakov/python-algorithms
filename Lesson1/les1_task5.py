# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
# https://app.diagrams.net/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&page-id=Non80xTPw9A1UWtK1Yfi&title=les1_diagram.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D15xNBhhB0Ye9kCCdbEjTMdzzZ1GgR_MwY%26export%3Ddownload
a = int(input('Введите первое число : '))
b = int(input('Введите второе число : '))
c = int(input('Введите третье число : '))
if (abs(a)<abs(c)) and (abs(a)>abs(b)) :
    print(f'Среднее число {a}')
elif (abs(b)>abs(a)) and (abs(b)<abs(c)):
    print(f'Среднее число {b}')
else:
    print(f'Среднее число {c}')
