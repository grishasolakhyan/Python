import math
import pylab 
import random
import time
import matplotlib.pyplot as plt 

m=2**32
a=268435461
b=907612489
N=3000
n=int(N/2)

line_cong=[]
line_cong1=[]
line_cong2=[]

rand=[]
rand1=[]
rand2=[]

for i in range(N):
    rand.append(random.randint(0, 9999))
    rand[i]=rand[i]/10000
print (rand)

for i in range (n):
    rand1.append(rand[i])
    rand2.append(rand[N-i-1])
    
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

x=Line_cong(time.time(),N)

for i in range (n):
    line_cong1.append(x[i])
    line_cong2.append(x[N-i-2])
print(x)

pylab.figure (1)
pylab.scatter(line_cong1, line_cong2, color='blue', s=4)
#plt.plot(line_cong1, line_cong2)
plt.xlabel('r')
plt.ylabel('r=f(y)')

pylab.figure(2)
plt.scatter(rand1, rand2, color='red', s=4)
plt.xlabel('r')
plt.ylabel('r=f(y)')

plt.legend()
plt.show()
