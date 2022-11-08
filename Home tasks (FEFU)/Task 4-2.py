import math
class LoopErr(Exception): pass
eps=1e-3
a=0
s=0
imax=1000
x=int(input("ВВЕДИТЕ X: "))
a=x
s=a

try:
    i = 1
    while(abs(a)>eps):
        if (i>imax):
            raise LoopErr()
            break
        a*=(-1)*x*x/(2*i*(2*i+1))
        s+=a
        i+=1
except LoopErr:
    print("ОШИБКА")
else:
    print("S = ", s)
    sinx=math.sin(x)
    print("SIN = ", sinx)
print(i)