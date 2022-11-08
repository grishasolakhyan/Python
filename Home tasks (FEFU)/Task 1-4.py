print("<TASK №1-4>")
n=int(input("ENTER LIST DIMENSION:"))
M=[ [0]*n for i in range(n) ]
for i in range(n):
    for j in range(n):
        if (i==j):
            M[i][j]=1
        elif (i!=j):
            M[i][j]=0
print(M)