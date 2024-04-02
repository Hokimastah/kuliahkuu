def kursi(x,b,c):
    if x == b:
        c.append(1)
        return
    elif x > b :
        return
    kursi(x+1,b,c)
    kursi(x+3,b,c)
    kursi(x+5,b,c)
    return len(c)

x = 0
a = int(input())
b = list(map(int,input().split()))
c = []
d = []
e = []
for i in b:
    d.append(kursi(x,i,c))
    c = []
for i in range(1,a+1):
    e.append(i)

for i in e:
    print(f"SESI {i}: {d[i-1]}")