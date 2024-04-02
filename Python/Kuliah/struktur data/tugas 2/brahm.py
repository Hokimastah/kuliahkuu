a = input()
x = list(map(int, input().split()))
y = []
for i in x:
    if not y:
        y.append(i)
    elif y.count(i) >= 1:
        y.remove(i)
    else:
        y.append(i)
print(len(y))