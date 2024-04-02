a = list(map(int,input().split()))
b = list(range(1,a[0]+1))
for i in b:
    if i % a[1] == 0:
        b[b.index(i)]= '*'
    else :
        b[b.index(i)]= str(i)

x = " ".join(b)
print(x)