def ms(x,y):
    for i in range(len(x)):
        y.append(min(x))
        x.remove(min(x))
    return

a = list(map(int,input().split()))
b = []
print(ms(a,b))