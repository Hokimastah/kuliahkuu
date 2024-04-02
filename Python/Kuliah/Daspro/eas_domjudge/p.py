n = int(input())
mboh = list(map(int,input().split()))

def ntah(mboh,n):
    if n == 1:
        print(mboh[0])
    elif n == 2:
        x = mboh[1]-mboh[0]
        print(mboh[-1]+x)
    elif n == 3:
        x = []
        x.append(mboh[1]-mboh[0])
        x.append(mboh[2]-mboh[1])
        a = x[1]-x[0]
        print(x[-1]+a+mboh[-1])
    elif n == 4:
        x = []
        x.append(mboh[1]-mboh[0])
        x.append(mboh[2]-mboh[1])
        x.append(mboh[3]-mboh[2])
        y = []
        y.append(x[1]-x[0])
        y.append(x[2]-x[1])
        a = y[1]-y[0]
        print(a+y[-1]+x[-1]+mboh[-1])
    elif n == 5:
        x = []
        x.append(mboh[1]-mboh[0])
        x.append(mboh[2]-mboh[1])
        x.append(mboh[3]-mboh[2])
        x.append(mboh[4]-mboh[3])
        y = []
        y.append(x[1]-x[0])
        y.append(x[2]-x[1])
        y.append(x[3]-x[2])
        z = []
        z.append(y[1]-y[0])
        z.append(y[2]-y[1])
        a = z[1]-z[0]
        print(a+z[-1]+y[-1]+x[-1]+mboh[-1])

ntah(mboh,n)