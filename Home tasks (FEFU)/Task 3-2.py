try:
	file = open('3_2.txt', 'r')
except Exception as err:
	print(err)
arr1=[]
arr2=[]
last_name=[]
year_search=[]

file = open('3_2.txt', 'r')
lines = file.read() 
file.close() 

print('СПИСОК ДАННЫХ:' + '\n' + lines + '\n') 
arr2 = lines.split('\n') 
for i in range(len(arr2)): 
    arr1.append(arr2[i].split()) 
    arr1[i][2] = str(arr1[i][2])

last_name=arr1.copy()

ln=0
last_name.sort(key=lambda i:i[0])
print("ОТСОРТИРОВАННЫЙ СПИСОК ПО ФАМИЛИИ:")
for i in last_name:
    print(i)

count=0
year=str(input("ВВЕДИТЕ ГОД РОЖДЕНИЯ:"))
for i in range(len(arr1)):
    if (arr1[i][2]==year):
        count+=1
        index=i
        for j in range(3):
            year_search.append(arr1[index][j])
if(count>0):
    print(year_search)
elif(count==0):
    print ("ТАКОГО ГОДА НЕТ В СПИСКЕ")