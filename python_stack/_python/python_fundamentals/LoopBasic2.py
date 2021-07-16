def biggie(list):
    for i in range(0,len(list),1):
        if(list[i]>0):
            list[i]="big"
    return list
list=[-1,3,4,5,-2]
print(biggie(list))

def countpositives(list):
    count=0
    for i in list:
        if(i>0):
            count=count+1
    list[len(list)-1]=count
    return list

clist=[-1,-4,-5,2,3,5,-9]
print(countpositives(clist))

def sumtot(list):
    sum=0;
    for i in list:
        sum=sum+i
    return sum

slist=[1,2,3,4,5]
print(sumtot(slist))

def avg(list):
    sum=0;
    for i in list:
        sum=sum+i
    return sum/len(list)

print(avg(slist))

def min(list):
    min=1000000000
    for i in list:
        if(i<min):
            min=i
    return min

print(min(slist))

def max(list):
    max=0
    for i in list:
        if(i>max):
            max=i
    return max

print(max(slist))

def ultanalsys(list):
    ult = {
        'sum_total': None,
        'maximum': None,
        'minimum': None,
        'average': None,
        'length': 0
    }
    ult['sum_total']=sumtot(list)
    ult['average']=avg(list)
    ult['minimum']=min(list)
    ult['maximum']=max(list)
    ult['length']=len(list)
    return ult

print(ultanalsys(slist))

def reverse_list(lst):
    half_len = int(len(lst) / 2)
    for i in range(half_len):
        lst[i] , lst[len(lst) - 1 - i] = lst[len(lst) - 1 - i], lst[i]
    return lst 

print(reverse_list([37, 2, 1, -9]))   






