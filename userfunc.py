#without argument,without return type
def add():
    print("without argument,without return type")
    a=5
    b=10
    print(a+b)
#without argument, with return type
def add1():
    print("without argument, with return type")
    a=5
    b=10
    return a+b
#with argument,without return type
def add3(a,b):
    print("with argument,without return type")
    print(a+b)
#with arguement,with return type
def add2(a,b):
    print("with arguement,with return type")
    return a+b
add()
print(add1())
add3(5,10)
print(add2(5,10))
