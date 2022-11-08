import random
n=9
f=[n]
for i in range(n):
    f.append(random.randint(-10,10))
print(f)
def maximum(f):
    f=list(f)
    k=f[0]
    for i in range (len(f)-1):
        if (k<f[i+1]):
            k=f[i+1]
    return k 
m=maximum(f)
print (m)