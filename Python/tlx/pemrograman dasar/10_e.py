a, b, k, x = map(int,input().split())
for i in range(k):
    x = abs(a*x+b)
print(x)