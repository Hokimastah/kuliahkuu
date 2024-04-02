def prima(x):
    if x == 2:
        return True
    elif x == 1:
        return False
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

x = int(input())
num = []
for i in range(x):
    a = int(input())
    num.append(a)
for i in num:
    if prima(i):
        print("YA")
    else:
        print("BUKAN")