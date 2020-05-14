# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
# https://app.diagrams.net/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=les1_diagram.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D15xNBhhB0Ye9kCCdbEjTMdzzZ1GgR_MwY%26export%3Ddownload
x = int(input("Введите трехзначное число : "))
a = x // 100
b = (x % 100) // 10
c = x  % 10
print(f'сумма равна : {a + b + c}')
print(f'произвдедение равно : {a * b * c}')
