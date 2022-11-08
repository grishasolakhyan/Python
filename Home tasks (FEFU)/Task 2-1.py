import math
print("<TASK №2-1>")
a=float(input("ENTER LEG A="))
b=float(input('ENTER LEG B='))

def gip(a, b):
    return (math.sqrt(a**2+b**2))
g=gip(a, b)
print("HYPOTENUSE C=", g, sep="")