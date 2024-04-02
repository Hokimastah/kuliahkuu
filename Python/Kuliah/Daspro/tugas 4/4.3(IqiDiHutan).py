a = int(input())
b = [0]
c = 1
for i in range (a-1) :
    b.append(c)
    c += (b[i]+b[i-1])

print(b[-1])