a, b = map(int,input().split())
c = []
for i in range(a, (b+1)):
    if i % 2 == 1 :
        c.append(i)

d = sum(c)
print(d)