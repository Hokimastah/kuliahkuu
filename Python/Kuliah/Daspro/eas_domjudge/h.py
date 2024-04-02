n = int(input())
id = []
ni = []
hg = []
kl = []
for i in range(n):
    ids, n, h, k = map(str,input().split())
    id.append(int(ids))
    ni.append(n)
    hg.append(int(h))
    kl.append(int(k))

def harga(a,b):
    x = []
    for i in range(len(b)):
        if b[i] == min(b):
            x.append(i)
    y = []
    for i in x:
        y.append(a[i])
    z = a.index(min(y))
    return z
def kualitas(a,b):
    x = []
    for i in range(len(b)):
        if b[i] == max(b):
            x.append(i)
    y = []
    for i in x:
        y.append(a[i])
    z = a.index(min(y))
    return z
a = harga(id,hg)
b = kualitas(id,kl)
print(f"Best item for price is: {id[a]} {ni[a]} {hg[a]} {kl[a]}")
print(f"Best item for quality is : {id[b]} {ni[b]} {hg[b]} {kl[b]}")