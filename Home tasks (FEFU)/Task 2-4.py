import random
n=int(input("ВВЕДИТЕ ДЛИНУ СПИСКА N="))
f=[n]
for i in range(n):
    f.append(random.randint(-10,10))
print(f)
a=int(input("ВВЕДИТЕ НАЧАЛЬНЫЙ ИНДЕКС ДИАПАЗОНА ПОИСКА a="))
b=int(input("ВВЕДИТЕ КОНЕЧНЫЙ ИНДЕКС ДИАПАЗОНА ПОИСКА b="))
def maximum(f,a,b):
    f=list(f)
    for i in f[a:b+1]:
        k=max(f[a:b+1])
    return k
m=maximum(f,a,b)
print("ДИАПАЗОН ПОИСКА: ",f[a:b+1])
print (m)
