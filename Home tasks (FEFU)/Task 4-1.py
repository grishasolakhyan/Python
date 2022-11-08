a=['a','b','c','d','e','f']
#МЕТОД INDEX()

print(a)
while True:
    try:
        k=str(input("ВВЕДИТЕ СИМВОЛ ИЗ СПИСКА: "))
        x=a.index(k)
        break;
    except ValueError:
        print("ТАКОГО СИМВОЛА НЕТ! ПОВТОРИТЕ ПОПЫТКУ")
print(x)

#ОПЕРАЦИЯ ИНДЕКСИРОВАНИЯ []

while True:
    try:
        m=int(input("ВВЕДИТЕ ИНДЕКС: "))
        r=a[m-1]
        break;
    except IndexError:
        print("ИНДЕКС ЭЛЕМЕНТА НЕ НАЙДЕН")
print(r)