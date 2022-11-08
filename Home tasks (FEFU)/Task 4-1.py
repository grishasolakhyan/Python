print("<TASK №4-1>")
a=['a','b','c','d','e','f']
print(a)
while True:
    try:
        k=str(input("ENTER A CHARACTER FROM THE LIST: "))
        x=a.index(k)
        break;
    except ValueError:
        print("THERE IS NO SUCH SYMBOL! TRY AGAIN")
print(x)
while True:
    try:
        m=int(input("ENTER INDEX: "))
        r=a[m]
        break;
    except IndexError:
        print("ELEMENT INDEX NOT FOUND")
print(r)