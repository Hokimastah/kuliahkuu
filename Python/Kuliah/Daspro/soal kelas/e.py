a = list(map(int,input().split()))
N = a[0]
M = a[1]

b = list(map(int,input().split()))
K = int(input())
c = 0
for i in b :
    if i == K:
        c += 1

print(c)