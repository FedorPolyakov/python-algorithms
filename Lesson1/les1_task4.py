#Определить, является ли год, который ввел пользователь, високосным или не високосным.
# https://app.diagrams.net/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&page-id=iQajI5M-0b7Ouemyhnd9&title=les1_diagram.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D15xNBhhB0Ye9kCCdbEjTMdzzZ1GgR_MwY%26export%3Ddownload
x = int(input('Введите год : '))
if (x % 4 == 0):
    if (x % 100 == 0):
        if (x % 400 == 0):
            print('Год високосный')
        else:
            print('год не високосный')
    else:
        print('год високосный')
else:
    print('год не високосный')
