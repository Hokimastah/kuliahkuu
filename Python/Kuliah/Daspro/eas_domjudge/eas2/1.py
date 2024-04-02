def fibonacci(n):
    n+=1
    x = [0, 1]
    while len(x) < n:
        y = x[-1] + x[-2]
        x.append(y)
    return x[n-1]

a = int(input())
b = []
for i in range(a):
    x = input()
    b.append(x)
c = int(input())
d = []
for i in range(c):
    x = list(map(str,input().split()))
    d.append(x)
    
ntah = []   

for i in d:
    x = []
    y = int(i[0])
    if fibonacci(y)%2 == 0:
        continue
    else: 
        x.append(i[1])
        x.append(i[2])
    ntah.append(x)
    
def cek(a,b):
    x = []
    y = []
    for i in a:
        if i == b[0]:
            x.append(a.index(i))
        elif i == b[1]:
            y.append(a.index(i))
    for i in x:
        a[i] = b[1]
    for i in y:
        a[i] = b[0]

for i in ntah:
    cek(b,i)

for i in b:
    print(i)