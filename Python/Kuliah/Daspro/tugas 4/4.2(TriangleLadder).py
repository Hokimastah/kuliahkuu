a = int(input())
b = list(map(int,input().split()))
def tambah(x) :
    c = []
    for i in range(len(x)-1) :
       c.append(x[i] + x[i+1])
    return c

res = [b]
while len(b) > 1:
    c = tambah(b)
    b = c
    res.append(c)

res.reverse()
for e in res:
    print(" ".join(map(str, e)))