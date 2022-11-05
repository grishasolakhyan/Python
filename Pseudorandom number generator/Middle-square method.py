import random
import pylab
import matplotlib.pyplot as plt 
class NonEightDigitNumber(Exception): pass
class NegativeNumber(Exception): pass
class Zero(Exception): pass

tim=int
n_s=str
N=1000
n=int(N/2)
mov=0
M=0
D=0

med_sqr=[]
med_sqr1=[]
med_sqr2=[]

med_multi=[]
rand=[]
rand1=[]
rand2=[]


#______________________________________________
for i in range(N):
    rand.append(random.randint(0, 9999))
    rand[i]=rand[i]/10000
print (rand)

for i in range (n):
    rand1.append(rand[i])
    rand2.append(rand[N-i-1])
    
def Med_Sqr(x, mov):
    tim=int
    if(x<0):
        raise NegativeNumber()
    elif(x>9999):
        raise NonEightDigitNumber()
    elif (x==0):
        raise Zero()
    
    if(mov>9):
        mov=1
    if (x//1000==0):
        x=x+mov*1000
    x0=x//100
    if (x0%10==0):
        mov=mov+1
        if(mov>9):
            mov=1
        x=x+mov*100
    x0=x//10
    if (x0%10==0):
        mov=mov+1
        if(mov>9):
            mov=1
        x=x+mov*10
    if (x%10==0):
        mov=mov+1
        if(mov>9):
            mov=1
        x=x+1

    tim=x*x
    tim=tim//100
    tim=tim%10000
    tim=tim/10000
    return tim, mov

def frequency_analysis_method(med_sqr1, n, step):
    st=1/step
    s_t0=-st
    s_t1=0
    an=[]
    ind=[]
    for i in range (step):
        s_t0=s_t0+st
        s_t1=s_t1+st
        k=0
        for j in range(len(med_sqr1)):
            if (s_t0<med_sqr1[j]<=s_t1):
                k=k+1
        an.append(k)
    
    for i in range(len(an)):
        an[i]=(an[i]/n)*100
        ind.append(i+1)
        
    return an, ind

def expected_value_and_variance(med_sqr):
    sum_m=0
    M=sum(med_sqr)/N
    for i in range(len(med_sqr)):
        sum_m=sum_m+(med_sqr[i])**2
    D=sum_m/N
    return M,D

def correlation(med_sqr):
    ind2=[]
    R=[]
    for i in range(1,N):
        ter=[]
        for j in range(i):
            ter.append(med_sqr[j]*med_sqr[j+1])
        R.append((sum(ter)/i)*12-3)
        ind2.append(i)
    return R, ind2       
            
while True:
    try:
        x=int(input("ВВЕДИТЕ ЧЕТЫРЁХЗНАЧНОЕ ЧИСЛО: "))
        i=0
        for i in range(N):
            if(mov>9):
                mov=1
            f, ma =Med_Sqr(x, mov)
            
            if f in med_sqr:
                x=f*10000
                x=int(x)
                x_str2=''
                x_str1=str(x)
                x_str2=x_str1[::-1]
                f=int(x_str2)
                f=f/10000
                med_sqr.append(f)
            else:
                med_sqr.append(f)  
            
            x=f*10000
            x=int(x)
            
            mov=ma
        break
    except NegativeNumber:
        print('ОТРИЦАТЕЛЬНОЕ ЧИСЛО')
    except Zero:
        print('НУЛЬ')
    except NonEightDigitNumber:
        print('СЛИШКОМ БОЛЬШОЕ ЧИСЛО')
#print(med_sqr)

for i in range (n):
    med_sqr1.append(med_sqr[i])
    med_sqr2.append(med_sqr[N-i-1])

step=int(input("УКАЖИТЕ КОЛИЧЕСТВО РАЗБИЕНИЙ: "))
analysis_stroke, ind=frequency_analysis_method(med_sqr1, n, step)
print(analysis_stroke)
print(ind)

M,D=expected_value_and_variance(med_sqr)
R, ind2=correlation(med_sqr)

pylab.figure (1)
pylab.scatter(med_sqr1, med_sqr2, color='blue', s=4)
#plt.plot(med_sqr1, med_sqr2)
plt.xlabel('r')
plt.ylabel('r=f(y)')

pylab.figure(2)
plt.title('Служебный генератор rand')
plt.scatter(rand1, rand2, color='red', s=4)
plt.xlabel('r')
plt.ylabel('r=f(y)')

pylab.figure(3)
plt.title('Частотный анализ')
plt.plot(ind, analysis_stroke, color='deeppink')
plt.scatter(ind, analysis_stroke, color='black', s=4)
plt.ylabel('fi, %')

pylab.figure(4)
plt.title('Математическое ожидание и дисперсия', size=15)
plt.text(0.1, 0.5, 'M={0}\nD={1}'.format(M, D), size=20)

pylab.figure(5)
plt.title('Корреляция')
#plt.scatter(ind2, R, color='red', s=4)
plt.plot(ind2, R, color='steelblue')

plt.legend()
plt.show()



