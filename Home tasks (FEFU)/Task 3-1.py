try:
	f = open('3_1.txt', 'r')
except Exception as err:
	print(err)
a=[]
file1=open('3_1.txt', 'r')
line=file1.readline()
a=[int (x) for x in line.split()]
file1.close()
print("ВЕСЬ СПИСОК:", a, sep="")
k1=a[0]
for i in range (len(a)-1):
    if(k1<a[i+1]):
        k1=a[i+1]
        ind1=i+1

k2=a[0]
for i in range (len(a)-1):
    if(a[i+1]<k2):
        k2=a[i+1]  
        ind2=i
a.pop(ind1)
a.pop(ind2)
print("ОБНОВЛЕННЫЙ СПИСОК:", a, sep="")
print ("МАКСИМАЛЬНОЕ ЧИСЛО:", k1, sep="")
print ("МИНИМАЛЬНОЕ ЧИСЛО:", k2, sep="")
with open('3_1w.txt', 'w') as file2:
    file2.writelines(str(a))