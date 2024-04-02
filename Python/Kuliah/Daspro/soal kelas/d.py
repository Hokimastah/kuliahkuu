a = list(map(int,input().split()))
b = str(sum(a) // 5)
c = str((sum(a) % 5)*20)
d = []
d.append(b)
d.append(c)

print(d[0]+'.'+d[1])