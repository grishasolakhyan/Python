import random
import pylab 
import matplotlib.pyplot as plt 
class NonSixDigitNumber(Exception): pass
class NegativeNumber(Exception): pass
class Zero(Exception): pass

x=int
x_check=int
x_check_tmp=int
N=3000
n=int(N/2)
mov=0

rand=[]
rand1=[]
rand2=[]

mixing=[]
mixing1=[]
mixing2=[]


for i in range(N):
    rand.append(random.randint(0, 9999))
    rand[i]=rand[i]/10000
print (rand)

for i in range (n):
    rand1.append(rand[i])
    rand2.append(rand[N-i-1])
    
def Checking(x_check, mov):
    if(x_check//10**5==0):
        mov=mov+1
        if(mov>9):
            mov=1
        x_check=x_check+mov*10**5
    
    x_check_tmp=x_check//10**4
    if(x_check_tmp==0):
        mov=mov+1
        if(mov>9):
            mov=1
        x_check=x_check+mov*10**4
        
    x_check_tmp=x_check//10**3
    if(x_check_tmp==0):
        mov=mov+1
        if(mov>9):
            mov=1
        x_check=x_check+mov*10**3
        
    x_check_tmp=x_check//10**2
    if(x_check_tmp==0):
        mov=mov+1
        if(mov>9):
            mov=1
        x_check=x_check+mov*10**2
    
    x_check_tmp=x_check//10
    if(x_check%10==0):
        mov=mov+1
        if(mov>9):
            mov=1
        x_check=x_check+mov*10
    
    if(x_check%10==0):
        mov=mov+1
        if(mov>9):
            mov=1
        x_check=x_check+mov
    x_ch=x_check
    return x_ch, mov

def Mixing(x, mov):
    if(x<0):
        raise NegativeNumber()
    elif(x>999999):
        raise NonSixDigitNumber()
    elif(x==0):
        raise Zero()
    
    x_check=x
    x1, mov=Checking(x_check, mov)
    
    x_str=str(x1)
    
    x_str1=''
    for i in range(4):
        x_str1=x_str1+x_str[i+2]
    for i in range(2):
        x_str1=x_str1+x_str[i]
    
    x_str2=''
    for i in range(2):
        x_str2=x_str2+x_str[i+4]
    for i in range(4):
        x_str2=x_str2+x_str[i]    
    
    x1=int(x_str1)
    x2=int(x_str2)
        
    tmp=x1+x2
    if(tmp>999999):
        tmp=tmp%10**6
    tmp=tmp/10**6
    return tmp, mov

while True:
    try:
        x=int(input("ВВЕДИТЕ ШЕСТИЗНАЧНОЕ ЧИСЛО: "))
        i=0
        for i in range (N):
            x, mov=Mixing(x, mov)
            
            if x in mixing:
                x_duo=x*10**5
                x_duo=int(x_duo)
                x_str2=''
                x_str1=str(x_duo)
                x_str2=x_str1[::-1]
                x=int(x_str2)
                x=x/100000
                mixing.append(x)
            else:
                mixing.append(x)  
            x=x*100000
        break
    except NegativeNumber:
        print('ОТРИЦАТЕЛЬНОЕ ЧИСЛО')
    except Zero:
        print('НУЛЬ')
    except NonSixDigitNumber:
        print('СЛИШКОМ БОЛЬШОЕ ЧИСЛО')

print (mixing)
        
for i in range (n):
    mixing1.append(mixing[i])
    mixing2.append(mixing[N-i-1])

pylab.figure (1)
pylab.scatter(mixing1, mixing2, color='blue', s=4)
#plt.plot(mixing1, mixing2)
plt.xlabel('r')
plt.ylabel('r=f(y)')

pylab.figure(2)
plt.scatter(rand1, rand2, color='red', s=4)
plt.xlabel('r')
plt.ylabel('r=f(y)')

plt.legend()
plt.show()
