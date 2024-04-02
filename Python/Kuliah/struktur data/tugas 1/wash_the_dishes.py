a = int(input())
kotor = list(range(1,a+1))
kotor.reverse()
sabun = []
bersih = []

m = int(input())
for i in range(m):
    x = list(map(int,input().split()))
    if x[0] == 1:
        for j in range(x[1]):
            if not kotor:
                break
            else : sabun.append(kotor.pop())
    elif x[0] == 2:
        for j in range(x[1]):
            if not sabun:
                break
            else : bersih.append(sabun.pop())

x = [len(kotor),len(sabun),len(bersih)]
x = max(x)
if not kotor :
    kotor.append("-")
elif not kotor.count("-") : kotor.reverse()
while len(kotor)<x:
    kotor.append(" ")
if not sabun :
    sabun.append("-")
elif not sabun.count("-") : sabun.reverse()
while len(sabun)<x:
    sabun.append(" ")
if not bersih :
    bersih.append("-")
elif not bersih.count("-") : bersih.reverse()
while len(bersih)<x:
    bersih.append(" ")

for i in range(x):
    print(F"{kotor[i]} {sabun[i]} {bersih[i]}")