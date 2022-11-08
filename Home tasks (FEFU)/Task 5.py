class geom_shape:
    def __init__(self,thick_line,color_line,color_shape):
        self.__thick_line=thick_line
        self.__color_line=color_line
        self.__color_shape=color_shape
    def __str__(self):
        inf = "ИНФОРМАЦИЯ О ГЕОРМЕТРИЧЕСКОЙ ФИГУРЕ: " + str(self.__thick_line) + "," + str(self.__color_line) + "," + str(self.__color_shape)
        return inf
    @property
    def thick_line_det(self):
        return self.__thick_line
    @thick_line_det.setter
    def thick_line_det(self,x):
        if (x>0):
            self.__thick_line=x
        else:
            raise ValueError("ЗНАЧЕНИЕ МЕНЬШЕ НУЛЯ")
    @property
    def color_line_det(self):
        return self.__color_line
    @color_line_det.setter
    def color_line_det(self,x):
        self.__color_line=x
    @property
    def color_shape_det(self):
        return self.__color_shape
    @color_shape_det.setter
    def color_shape_det(self,x):
        self.__color_shape=x

class circle(geom_shape):
    def __init__(self,thick_line,color_line,color_shape,radius):
        super().__init__(thick_line,color_line,color_shape)
        self.__radius=radius
    def s(self):
        s = 3.1415926535*self.__radius**2
        return s
    def __str__(self):
        inf = super().__str__() + ". РАДИУС КРУГА: " + str(self.__radius)
        return inf
    @property
    def radius_det(self):
        return self.__radius
    @radius_det.setter
    def radius_det(self, x):
        if (x>0):
            self.__radius=x
        else:
            raise ValueError("ЗНАЧЕНИЕ МЕНЬШЕ НУЛЯ")

class rectangle(geom_shape):
    def __init__(self,thick_line,color_line,color_shape,side1,side2):
        super().__init__(thick_line,color_line,color_shape)
        self.__side1=side1
        self.__side2=side2
    def s(self):
        s = self.__side1*self.__side2
        return s
    def __str__(self):
        inf = super().__str__() + ". СТОРОНЫ ПРЯМОУГОЛЬНИКА: " + str(self.__side1) + "," + str(self.__side2)
        return inf
    @property
    def side1_det(self):
        return self.__side1
    @side1_det.setter
    def side1_det(self, x):
        if (x>0):
            self.__side1=x
        else:
            raise ValueError("ЗНАЧЕНИЕ МЕНЬШЕ НУЛЯ")
    @property
    def side2_det(self):
        return self.__side2
    @side2_det.setter
    def side2_det(self,x):
        if (x>0):
            self.__side2=x
        else:
            raise ValueError("ЗНАЧЕНИЕ МЕНЬШЕ НУЛЯ")

class triangle(geom_shape):
    def __init__(self,thick_line,color_line,color_shape,base,height):
        super().__init__(thick_line,color_line,color_shape)
        self.__base=base
        self.__height=height
    def s(self):
        s = self.__base*self.__height*0.5
        return s
    def __str__(self):
        inf = super().__str__() + ". ОСНОВАНИЕ ТРЕУГОЛЬНИКА И ВЫСОТА: " + str(self.__base) + "," + str(self.__height)
        return inf
    @property
    def base_det(self):
        return self.__base
    @base_det.setter
    def base_det(self, x):
        if (x>0):
            self.__base=x
        else:
            raise ValueError("ЗНАЧЕНИЕ МЕНЬШЕ НУЛЯ")
    @property
    def height_det(self):
        return self.__height
    @height_det.setter
    def height_det(self, x):
        if (x>0):
            self.__height=x
        else:
            raise ValueError("ЗНАЧЕНИЕ МЕНЬШЕ НУЛЯ")

#ГЕОМЕРИЧЕСКАЯ ФИГУРА

a=geom_shape(21,"КРАСНЫЙ","ЧЕРНЫЙ")
print(a)
a.thick_line_det=12
print(a.thick_line_det)
a.color_line_det="СИНИЙ"
print(a.color_line_det)
a.color_shape_det="БЕЛЫЙ"
print(a.color_shape_det)

#КРУГ

b=circle(21,"БЕЛЫЙ","ЧЕРНЫЙ",150)
print("\n")
print(b)
print("ПЛОЩАДЬ ТРЕУГОЛЬНИКА: ", b.s())
b.radius_det=100
print(b.radius_det)

#ПРЯМОУГОЛЬНИК

c=rectangle(21,"ЧЕРНЫЙ","БЕЛЫЙ",400,200)
print("\n")
print(c)
print("ПЛОЩАДЬ ПРЯМОУГОЛЬНИКА: ", c.s())
c.side1_det = 300
c.side2_det = 100
print(c.side1_det)
print(c.side2_det)

#ТРЕУГОЛЬНИК

d=triangle(21,"РОЗОВЫЙ","ЧЕРНЫЙ",100,200)
print("\n")
print(d)
print("ПЛОЩАДЬ ТРЕУГЛЬНИКА: ", d.s())
d.base_det=50
d.height_det=100
print(d.base_det)
print(d.height_det)