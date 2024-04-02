j_hp = int(input())
hp = []
for i in range(j_hp):
    a = input()
    hp.append(a)

t_hp = int(input())
tukar = []
for i in range(t_hp):
    a = list(map(str,input().split()))
    tukar.append(a)

def cek(a,b):
    x = []
    y = []
    for i in a:
        if i == b[0]:
            x.append(a.index(i))
        elif i == b[1]:
            y.append(a.index(i))
    for i in x:
        a[i] = b[1]
    for i in y:
        a[i] = b[0]

for i in tukar:
    cek(hp,i)

for i in hp:
    print(i)