def countdown(a):
    down = []
    for i in range(a , 0, -1):
        down.append(i)
    return down
print(countdown(2))

def lisprint(printer):
    print(printer[0])
    return(printer[1])

print(lisprint(countdown(2)))

def firstplus(list):
    return(list[0] + len(list))

print(firstplus(countdown(2)))

def valuesgreat(list):
    if(len(list)>2):
        great = []
        for i in list:
            if(i>list[1]):
                great.append(i)
            return great
    else:
        return False

print(valuesgreat(countdown(2)))
print(valuesgreat(countdown(5)))

def lengthval(a,b):
    prinlist=[]
    for i in range(0, a, 1):
        prinlist.append(b)
    return prinlist

print(lengthval(7,7))

