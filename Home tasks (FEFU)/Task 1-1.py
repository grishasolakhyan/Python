import random
print("<TASK №1-1>")
a=[]
for i in range(10):
    a.append(random.randint(-10,10))
print("LIST:",a)
sum=0
for i in a:
    sum+=i
print("SUM=", sum)
Minimum=min(a)
Maximum=max(a)
print("MIN=",Minimum, sep="")
print("MAX=",Maximum, sep="")
k=0
for x in a:
    if x<0:
        k=k+1
print("NUMBER OF NEGATIVE NUMBERS=",k,sep="")