#Values types => string,number 

#!Bunların üzerinde yaptığımız zman kopyalama işlemi olur.
x = 5
y = 25

x = y 
y = 10

print(x,y)


#Reference types => list,class

#!Bunların üzerinde yaptığımız zaman değişme işlemi hafıza kaydetme işlemi olur.

x = ["banana","onion"]
y = ["banana","onion"]

x = y 
x[0] = "cucumber"

print(x,y)