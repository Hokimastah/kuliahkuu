a = int(input())
b = list(map(int,input().split()))
x = 0
y = 0
z = []
for i in b:
    if z.count(i)>0 :
        continue
    elif b.count(i)>=y:
        if i>x :
            y = b.count(i)
            x = i
    z.append(i)
print(x)