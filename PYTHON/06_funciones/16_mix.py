#cristianooooooooooooo


def funcion(a,b, *args, **kwargs):
    print("a=",a)
    print("b=",b)
    for arg in args:
        print("args=",arg)
    for key, value in kwargs.items():
        print (key ,"=", value)

funcion(1,2,3,4,5, x=3, y=5, z=7 , e="hola", r="como" ,t = "estas")
#salida
# a= 1
# b= 2
# args= 3
# args= 4
# args= 5
# x = 3
# y = 5
# z = 7
# e = hola
# r = como
# t = estas


def funcion(a,b, *args, **kwargs):
    print("a=",a)
    print("b=",b)
    for arg in args:
        print("args=",arg)
    for key, value in kwargs.items():
        print (key ,"=", value)

args = [3,4,5]

kwargs = {"x":3, "y":5, "z":7 , "e":"hola", "r":"como" ,"t":"estas"}

funcion(1,2,*args, **kwargs)
#salida
# a= 1
# b= 2
# args= 3
# args= 4
# args= 5
# x = 3
# y = 5
# z = 7
# e = hola
# r = como
# t = estas