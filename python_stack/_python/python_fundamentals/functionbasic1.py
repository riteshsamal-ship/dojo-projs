def a():
    return 5        # 5
print(a())

def a():
    return 5        # 10
print(a()+a())

def a():
    return 5
    return 10       # 5
print(a())

def a():
    return 5
    print(10)       # 5
print(a())

def a():
    print(5)        # 5 Null
x = a()
print(x)

def a(b,c):
    print(b+c)          # 3 5 null 
#print(a(1,2) + a(2,3))

def a(b,c):
    return str(b)+str(c)        # "25"
print(a(2,5))

def a():
    b = 100
    print(b)
    if b < 10:
        return 5               # 100 10
    else:
	    return 10
    return 7
print(a())

def a(b,c):
    if b<c:
        return 7
    else:                       # 7 14 21
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))

def a(b,c):
    return b+c
    return 10                  # 8
print(a(3,5))

b = 500
print(b)
def a():
    b = 300                   # 500 500 300 500
    print(b)
print(b)
a()
print(b)

b = 500
print(b)
def a():
    b = 300                    # 500 500 300 500
    print(b)
    return b
print(b)
a()
print(b)

b = 500
print(b)
def a():
    b = 300                 # 500 500 300 300
    print(b)
    return b
print(b)
b=a()
print(b)

def a():
    print(1)
    b()                     # 1 3 2
    print(2)
def b():
    print(3)
a()

def a():
    print(1)
    x = b()
    print(x)
    return 10           # 1 3 5 10
def b():
    print(3)
    return 5
y = a()
print(y)

