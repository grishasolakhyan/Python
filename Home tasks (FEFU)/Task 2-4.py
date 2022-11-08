import random
print("<TASK №2-4>")
n=int(input("ENTER LIST LENGTH N="))
f=[n]
for i in range(n):
    f.append(random.randint(-10,10))
print(f)
a=int(input("ENTER SEARCH RANGE START INDEX a="))
b=int(input("ENTER SEARCH RANGE END INDEX b="))
def maximum(f,a,b):
    f=list(f)
    for i in f[a:b+1]:
        k=max(f[a:b+1])
    return k
m=maximum(f,a,b)
print("SEARCH RANGE: ",f[a:b+1])
print (m)
