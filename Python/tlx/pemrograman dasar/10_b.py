ntah = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
nyoh = int(input())
step = []
for i in range(nyoh):
    x = list(map(str,input().split()))
    step.append(x)

for i in step:
    if i[0] == "A":
        if i[2] == "A":
            x = a[int(i[1])-1]
            a[int(i[1])-1] = a[int(i[3])-1]
            a[int(i[3])-1] = x
        elif i[2] == "B":
            x = a[int(i[1])-1]
            a[int(i[1])-1] = b[int(i[3])-1]
            b[int(i[3])-1] = x
    elif i[0] == "B":
        if i[2] == "A":
            x = b[int(i[1])-1]
            b[int(i[1])-1] = a[int(i[3])-1]
            a[int(i[3])-1] = x
        elif i[2] == "B":
            x = b[int(i[1])-1]
            b[int(i[1])-1] = b[int(i[3])-1]
            b[int(i[3])-1] = x

for i in range(ntah):
    a[i] = str(a[i])
    b[i] = str(b[i])
a = " ".join(a)
b = " ".join(b)
print(a)
print(b)