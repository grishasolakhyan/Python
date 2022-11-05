import random
import math
import time
import pylab
import numpy as np
import matplotlib.pyplot as plt 
class NonEightDigitNumber(Exception): pass
class NonSixDigitNumber(Exception): pass
class NegativeNumber(Exception): pass
class Zero(Exception): pass

tim=int
n_s=str
m=2**32
a=268435461
b=907612489
N=2000
n=int(N/2)
mov=0
M=0
D=0
q=10

final_array=[]
final_array1=[]
final_array2=[]

rand=[]
rand1=[]
rand2=[]

game=[]


for i in range(N):
    rand.append(random.randint(0, 9999))
    rand[i]=rand[i]/10000
print (rand)
print('\n')
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

def Line_cong(seed,N):
    if N==1:
        return math.ceil(math.fmod(a*math.ceil(seed)+b,m))
    r=[0 for i in range(N)]
    r[0]=math.ceil(seed)
    for i in range(1,N):
        r[i]=math.ceil(math.fmod((a*r[i-1]+b),m))
    for i in range(0,N):
        r[i]=r[i]*2.3/10**10
    return r[0:N]

def frequency_analysis_method(final_array1, n, step):
    st=1/step
    s_t0=-st
    s_t1=0
    an=[]
    ind=[]
    for i in range (step):
        s_t0=s_t0+st
        s_t1=s_t1+st
        k=0
        for j in range(len(final_array1)):
            if (s_t0<final_array1[j]<=s_t1):
                k=k+1
        an.append(k)
    
    for i in range(len(an)):
        an[i]=(an[i]/n)*100
        ind.append(i+1)
        
    return an, ind

def expected_value_and_variance(final_array):
    sum_m=0
    M=sum(final_array)/N #МАТЕМАТИЧЕСКОЕ ОЖИДАНИЕ
    
    mid_final_array=np.mean(final_array)
    for i in range(len(final_array)):
        sum_m=sum_m+(mid_final_array-final_array[i])**2
    D=sum_m/N #ДИСПЕРСИЯ
    return M,D

def correlation(final_array):
    ind2=[]
    R=[]
    for i in range(1,n):
        ter=[]
        for j in range(i):
            ter.append(final_array[j]*final_array[j+1])
        R.append((sum(ter)/i)*12-3)
        ind2.append(i)
    return R, ind2

def TheGame(game, q):      
    score=0
    game_generator=Line_cong(time.time(),q) 
    for i in range (q):
        game_generator[i]=game_generator[i]*10
        game_generator[i]=round(game_generator[i])
    for i in range (q):
        if(game[i]==game_generator[i]):
            score=score+1
    return score, game_generator

while True:
    try:
        print('СПИСОК МЕТОДОВ:'
              '\n_________________________________'
              '\n| 1)МЕТОД СЕРЕДИННЫХ КВАДРАТОВ   |'
              '\n| 2)МЕТОД СЕРЕДИННЫХ ПРОИЗВЕДЕНИЙ|'
              '\n| 3)МЕТОД ПЕРЕМЕШИВАНИЯ          |'
              '\n| 4)ЛИНЕЙНЫЙ КОНГРУЭНТНЫЙ МЕТОД  |'
              '\n| а может сыграете в лотерею?    |'
              '\n| 5)ЛОТЕРЕЯ                      |'
              '\n|________________________________|')
        number_of_method=int(input("ВЫБЕРИТЕ МЕТОД И НАЖМИТЕ ENTER: "))
        break
    except ValueError:
        print("ВВЕДЕНО НЕ ЦЕЛОЕ ЧИСЛО ИЛИ ВООБЩЕ НЕ ЧИСЛО")
if(number_of_method<5):     
    if(number_of_method==1):
        while True:
            try:
                x=int(input("ВВЕДИТЕ ЧЕТЫРЁХЗНАЧНОЕ ЧИСЛО И НАЖМИТЕ ENTER: "))
                i=0
                for i in range(N):
                    if(mov>9):
                        mov=1
                    f, ma =Med_Sqr(x, mov)
                    
                    if f in final_array:
                        x=f*10000
                        x=int(x)
                        x_str2=''
                        x_str1=str(x)
                        x_str2=x_str1[::-1]
                        f=int(x_str2)
                        f=f/10000
                        final_array.append(f)
                    else:
                        final_array.append(f)  
                    
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
        #print(final array)
        for i in range (n):
            final_array1.append(final_array[i])
            final_array2.append(final_array[N-i-1])
    elif(number_of_method==2):
        while True:
            try:
                x0=int(input("ВВЕДИТЕ ПЕРВОЕ ЧЕТЫРЁХЗНАЧНОЕ ЧИСЛО И НАЖМИТЕ ENTER: "))
                x1=int(input("ВВЕДИТЕ ВТОРОЕ ЧЕТЫРЁХЗНАЧНОЕ ЧИСЛО И НАЖМИТЕ ENTER: "))
                i=0
                for i in range(N):
                    
                    if(mov>9):
                        mov=1
                    x_0, x_1, ma=Med_Multi(x0, x1, mov)
                    
                    if x_1 in final_array:
                        x_duo=x_1*10000
                        x_duo=int(x_duo)
                        x_str2=''
                        x_str1=str(x_duo)
                        x_str2=x_str1[::-1]
                        x_1=int(x_str2)
                        x_1=x_1/10000
                        final_array.append(x_1)
                    else:
                        final_array.append(x_1)  
                        
                    x0=x_0
                    x1=x_1*10000
                break
            except NegativeNumber:
                print('ОТРИЦАТЕЛЬНОЕ ЧИСЛО')
            except Zero:
                print('НУЛЬ')
            except NonEightDigitNumber:
                print('СЛИШКОМ БОЛЬШОЕ ЧИСЛО')
        #print(final_array)  
        for i in range (n):
            final_array1.append(final_array[i])
            final_array2.append(final_array[N-i-1])
    elif(number_of_method==3):
        while True:
            try:
                x=int(input("ВВЕДИТЕ ШЕСТИЗНАЧНОЕ ЧИСЛО И НАЖМИТЕ ENTER: "))
                i=0
                for i in range (N):
                    x, mov=Mixing(x, mov)
                    
                    if x in final_array:
                        x_duo=x*10**5
                        x_duo=int(x_duo)
                        x_str2=''
                        x_str1=str(x_duo)
                        x_str2=x_str1[::-1]
                        x=int(x_str2)
                        x=x/100000
                        final_array.append(x)
                    else:
                        final_array.append(x)  
                    x=x*100000
                break
            except NegativeNumber:
                print('ОТРИЦАТЕЛЬНОЕ ЧИСЛО')
            except Zero:
                print('НУЛЬ')
            except NonSixDigitNumber:
                print('СЛИШКОМ БОЛЬШОЕ ЧИСЛО')
        
        #print (final_array)
        
        for i in range (n):
            final_array1.append(final_array[i])
            final_array2.append(final_array[N-i-1])
    
    elif(number_of_method==4):
        final_array=Line_cong(time.time(),N) 
        for i in range (n):
            final_array1.append(final_array[i])
            final_array2.append(final_array[N-i-2])
        
        #print(x)
    
    step=int(input("УКАЖИТЕ КОЛИЧЕСТВО РАЗБИЕНИЙ И НАЖМИТЕ ENTER: "))
    analysis_stroke, ind=frequency_analysis_method(final_array1, n, step)
    print(analysis_stroke)
    
    M,D=expected_value_and_variance(final_array)

    R, ind2=correlation(final_array)
    
    pylab.figure (1)
    if(number_of_method==1):
        plt.title('Метод серединных квадратов при N={0}'.format(n), size=15)
    elif(number_of_method==2):
        plt.title('Метод серединных произведений при N={0}'.format(n), size=15)
    elif(number_of_method==3):
        plt.title('Метод перемешивания при N={0}'.format(n), size=15)
    elif(number_of_method==4):
        plt.title('Линейный конгруэнтный метод при N={0}'.format(n), size=15)
    pylab.scatter(final_array1, final_array2, color='blue', s=4)
    #plt.plot(final_array1, final_array2)
    plt.xlabel('r', size=15)
    plt.ylabel('r=f(y)', size=15)
    
    pylab.figure(2)
    plt.title('Служебный генератор rand при N={0}'.format(n), size=15)
    plt.scatter(rand1, rand2, color='red', s=4)
    plt.xlabel('r', size=15)
    plt.ylabel('r=f(y)', size=15)
    
    pylab.figure(3)
    plt.title('Частотный анализ при N={0}'.format(n), size=15)
    plt.plot(ind, analysis_stroke, color='deeppink')
    plt.scatter(ind, analysis_stroke, color='black', s=4)
    plt.ylabel('fi, %', size=15)
    
    pylab.figure(4)
    plt.title('Математическое ожидание и дисперсия при N={0}'.format(n), size=15)
    plt.text(0.1, 0.5, 'M={0}\nD={1}'.format(M, D), size=20)
    
    pylab.figure(5)
    plt.title('Корреляция при N={0}'.format(n), size=15)
    #plt.scatter(ind2, R, color='red', s=4)
    plt.plot(ind2, R, color='indigo')
    
    
    plt.legend()
    plt.show()
elif(number_of_method==5):
    bank=100
    while(number_of_method!=0):
        doub=int
        game=[]
        print("ВАШ СЧЁТ СОСТАВЛЯЕТ $",bank)
        print('У ВАС ЕСТЬ ЛОТЕРЕЙНЫЙ БИЛЕТ ДЛЯ 10 ЧИСЕЛ ОТ 1 ДО 99!'
              '\nВЫБЕРИТЕ И ВВЕДИТЕ 10 ЧИСЕЛ ИЗ ДАННОГО ДИАПАЗОНА:')
        for i in range(q):
            game.append(int(input()))
        print('ВАШ ЛОТЕРЕЙНЫЙ БИЛЕТ:', game, sep='')
        score, game_generator=TheGame(game, q)
        print('ВЫПАВШИЕ ЧИСЛА:      ', game_generator, sep='')
        print("")
        print('УГАДАННЫХ ЧИСЕЛ: ', score, sep='')
        print("")
        if(score==0):
            print("К СОЖАЛЕНИЮ ВЫ НИЧЕГО НЕ ВЫЙГРАЛИ,"
                  "\nНО ВОЗМОЖНО В СЛЕДУЮЩИЙ РАЗ ВАМ ПОВЕЗЁТ")
            print("")
        elif(0<score<3):
            bank=bank+50
            print("ВЫ ВЫЙГРАЛИ $50")
        elif(2<score<5):
            bank=bank+100
            print("ВЫ ВЫЙГРАЛИ $100")
        elif(5<score<8):
            bank=bank+250
            print("ВЫ ВЫЙГРАЛИ $250")
        elif(score==8):
            bank=bank+500
            print("ВЫ ВЫЙГРАЛИ $500")
        elif(score==9):
            bank=bank+1000
            print("ВЫ ВЫЙГРАЛИ $1000")
        elif(score==10):
            bank=bank+10000
            print("ВЫ ВЫЙГРАЛИ $10000")
        print("ВАШ СЧЁТ СОСТАВЛЯЕТ $", bank,"\n")
       
        print("ХОТИТЕ ЗАБРАТЬ СВОИ ДЕНЬГИ И УЙТИ ИЛИ ПРОДОЛЖИТЬ ИГРУ?")
        print("НАЖМИТЕ 0, ЧТОБЫ ЗАБРАТЬ ДЕНЬГИ И ПОКИНУТЬ ИГРУ\n"
              "НАЖМИТЕ 9, ЧТОБЫ ПРОДОЛЖИТЬ ИГРУ ЗА $50")
        print("")
        while(doub!=0 and doub!=9):
            doub=int(input("ВВЕДИТЕ НОМЕР КОМАНДЫ И НАЖМИТЕ ENTER:"))
            if(doub==0):
                n_u=doub
                print("ВАШ СЧЁТ СОСТВАЛЯЕТ $", bank, "\n"
                      "БЛАГОДАРИМ ВАС ЗА ИГРУ")
            elif(doub==9):
                if(bank>=50):
                    n_u=doub
                    print("ЧТО Ж, ТОГДА ПРОДОЛЖИМ ИГРУ")
                    print("")
                    bank=bank-50
                elif(bank<50):
                    n_u=0
                    print("У ВАС НЕДОСТАТОЧНО ДЕНЕГ НА СЧЕТУ. К СОЖАЛЕНИЮ ВЫ ПОКИДАЕТЕ ИГРУ\n"
                          "ВАШ СЧЁТ СОСТВАЛЯЕТ $",bank)
            number_of_method=n_u