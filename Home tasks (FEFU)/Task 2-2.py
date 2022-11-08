print("<TASK №2-2>")
r=float(input("ENTER CIRCLE RADIUS R="))

def sq_len(r):
    return 3.1415*r**2, 2*3.1415*r
s, l=sq_len(r)
print("The area is: ",s, " | Circle length: ", l, sep="")