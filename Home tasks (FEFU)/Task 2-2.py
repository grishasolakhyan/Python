r=float(input("ВВЕДИТЕ РАДИУС ОКРУЖНОСТИ R="))

def sq_len(r):
    return 3.1415*r**2, 2*3.1415*r
s, l=sq_len(r)
print("Площадь равна: ",s, " | Длина круга: ", l, sep="")