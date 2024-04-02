a, d = map(int,input().split())
idx = [range(0,a)]
x = []
y = []
for i in range(a):
    xi, yi = map(int,input().split())
    x.append(xi)
    y.append(yi)

def pangkat(a,b):
    if b == 0:
        return 1
    x = 0
    while x<b-1:
        x+=1
        a*=a
    return a

hasil = []
for i in range(a):
    for j in range(a):
        if j == i:
            continue
        hasil.append(pangkat(abs(x[i]-x[j]),d)+pangkat(abs(y[i]-y[j]),d))

maks = max(hasil)
mini = min(hasil)
print(f"{mini} {maks}")