# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.
# https://app.diagrams.net/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&page-id=A7CKvdCOF4zmbLFLpn9X&title=Lesson2Diagram.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1u_CqrRwx8lLYnRztQi1fgedMtYm90-N-%26export%3Ddownload
def reverse(x):
    if int(x) == 0:
        return x
    else:
        y = ''
        while True:
            if int(x) % 10 == 0:
                x = int(x) // 10
            else:
                break
        for i in str(x):
               y = i + y
        return y

x = int(input('Введите число: '))
z = reverse(x)
print(z)
