a = int(input())
b = [0]
c = 1
"""def kocak(init, n, i=1):
    if n <= len(init): return sum(init)
    init.append(init[i-2]+init[i-1])
    print(init[i-2], init[i-1])
    return kocak(init, n, i+1)

print(kocak([0,1], a, 1))"""


for i in range (a-1) :
    b.append(c)
    c += b[i]
d = sum(b)*125
print(d)