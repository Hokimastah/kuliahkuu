j_hp = int(input())
hp = []
for i in range(j_hp):
    a = input()
    hp.append(a)

t_hp = int(input())
tukar = []
for i in range(t_hp):
    a = list(map(input().split()))
    tukar.append(a)

for i in range(len(tukar)):
    a = hp.index(tukar[i][0])
    b = hp.index(tukar[i][1])
    hp[a] = tukar[i][1]
    hp[b] = tukar[i][0]

for i in hp:
    print(i)