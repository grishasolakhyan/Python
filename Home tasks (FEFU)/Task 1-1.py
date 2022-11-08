#ЗАДАНИЕ 1
print("ЗАДАНИЕ №1")
import random
a=[]
for i in range(10):
    a.append(random.randint(-10,10))
print("СПИСОК:",a)
sum=0
for i in a:
    sum+=i
print("СУММА=", sum)
Minimum=min(a)
Maximum=max(a)
print("МИНИМУМ=",Minimum, sep="")
print("МАКСИМУМ=",Maximum, sep="")
k=0
for x in a:
    if x<0:
        k=k+1
print("КОЛИЧЕСТВО ОТРИЦАТЕЛЬНЫХ ЧИСЕЛ=",k,sep="")