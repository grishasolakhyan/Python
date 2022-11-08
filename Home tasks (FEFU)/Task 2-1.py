import math
a=float(input("ВВЕДИТЕ КАТЕТ а="))
b=float(input('ВВЕДИТЕ КАТЕТ b='))

def gip(a, b):
    return (math.sqrt(a**2+b**2))
g=gip(a, b)
print("ГИПОТЕНУЗА c=", g, sep="")