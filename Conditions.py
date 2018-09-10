import sys

def is_leap(year):
    leap = False

    if year%400 ==0:
        leap=True
    elif year%100 ==0:
        pass
    elif year%4 == 0:
        leap=True
    else:
        pass
    return leap

year = int(input())
print(is_leap(year))
n = int(input())
for i in range(1,n+1):
    print(i,end='')#print without space
