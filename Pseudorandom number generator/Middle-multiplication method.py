import random
import pylab 
import matplotlib.pyplot as plt 
class NonEightDigitNumber(Exception): pass
class NegativeNumber(Exception): pass
class Zero(Exception): pass

N=5000
n=int(N/2)

rand=[]
rand1=[]
rand2=[]

med_multi=[]
med_multi1=[]
med_multi2=[]

mov=0

for i in range(N):
    rand.append(random.randint(0, 9999))
    rand[i]=rand[i]/10000
print (rand)

for i in range (n):
    rand1.append(rand[i])
    rand2.append(rand[N-i-1])
    
def Med_Multi(x0, x1, mov):
    if(x0<0 or x1<0):
        raise NegativeNumber()
    elif(x0>9999 or x1>9999):
        raise NonEightDigitNumber()
    elif (x0==0 or x1==0):
        raise Zero()
        
    if(mov>9):
        mov=1
    if (x0//1000==0):
        x0=x0+mov*1000
    x_tmp=x0//100
    if (x_tmp%10==0):
        mov=mov+1
        if(mov>9):
            mov=1
        x0=x0+mov*100
    x_tmp=x0//10
    if (x_tmp%10==0):
        mov=mov+1
        if(mov>9):
            mov=1
        x0=x0+mov*10
    if (x0%10==0):
        mov=mov+1
        if(mov>9):
            mov=1
        x0=x0+1
        
    if(mov>9):
        mov=1
    if (x1//1000==0):
        x1=x1+mov*1000
    x_tmp=x1//100
    if (x_tmp%10==0):
        mov=mov+1
        if(mov>9):
            mov=1
        x1=x1+mov*100
    x_tmp=x1//10
    if (x_tmp%10==0):
        mov=mov+1
        if(mov>9):
            mov=1
        x1=x1+mov*10
    if (x1%10==0):
        mov=mov+1
        if(mov>9):
            mov=1
        x1=x1+1
    
    tim=x0*x1
    tim=tim//100
    tim=tim%10000
    tim=tim/10000
    return x0, tim, mov

while True:
    try:
        x0=int(input("ВВЕДИТЕ ПЕРВОЕ ЧЕТЫРЁХЗНАЧНОЕ ЧИСЛО: "))
        x1=int(input("ВВЕДИТЕ ВТОРОЕ ЧЕТЫРЁХЗНАЧНОЕ ЧИСЛО: "))
        i=0
        for i in range(N):
            
            if(mov>9):
                mov=1
            x_0, x_1, ma=Med_Multi(x0, x1, mov)
            
            if x_1 in med_multi:
                x_duo=x_1*10000
                x_duo=int(x_duo)
                x_str2=''
                x_str1=str(x_duo)
                x_str2=x_str1[::-1]
                x_1=int(x_str2)
                x_1=x_1/10000
                med_multi.append(x_1)
            else:
                med_multi.append(x_1)  
                
            x0=x_0
            x1=x_1*10000
        break
    except NegativeNumber:
        print('ОТРИЦАТЕЛЬНОЕ ЧИСЛО')
    except Zero:
        print('НУЛЬ')
    except NonEightDigitNumber:
        print('СЛИШКОМ БОЛЬШОЕ ЧИСЛО')
#print(med_multi)

for i in range (n):
    med_multi1.append(med_multi[i])
    med_multi2.append(med_multi[N-i-1])
    
pylab.figure (1)
pylab.scatter(med_multi1, med_multi2, color='blue', s=4)
#plt.plot(med_multi1, med_multi2)
plt.xlabel('r')
plt.ylabel('r=f(y)')

pylab.figure(2)
plt.scatter(rand1, rand2, color='red', s=4)
plt.xlabel('r')
plt.ylabel('r=f(y)')

plt.legend()
plt.show()