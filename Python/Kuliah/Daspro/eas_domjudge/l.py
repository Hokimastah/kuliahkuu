n = int(input())
m1 = []
k1 = []
for i in range(n):
    m, k = map(int,input().split())
    m1.append(m)
    k1.append(k)

def urutan(a,b):
    x = []
    for i in range(1,a+1):
        x.append(i)
    y = []
    while len(y)<b:
        if len(x) == 1:
            y.append(x)
            break
        x.append(x[1])
        y.append(x[0])
        x.remove(x[0])
        x.remove(x[0])
    return y[-1]

hasil = []
for i in range(n):
    x = urutan(m1[i],k1[i])
    hasil.append(x)

for i in hasil:
    print(i)