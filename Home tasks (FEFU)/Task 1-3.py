import random
print("<TASK №1-3>")
f=[]
for i in range(100):
    f.append(random.randint(-10,10))
print(f)
print("\n")
for x in range(0,10):
    x=x*10
    print(f[x:x+10])
print("\n")
u=[]
u=f[4:100:5]
print("EVERY 5TH ELEMENT OF LIST:",u, sep="")
print("\n")
for y in range(len(f)):
	if f[y] % 2 != 0:
		f[y]=f[y]+1
for x in range(0,10):
    x=x*10
    print(f[x:x+10])