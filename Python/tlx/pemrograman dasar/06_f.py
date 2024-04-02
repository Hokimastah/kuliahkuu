x = int(input())
a = list(range(1,x+1))
a.reverse()
for i in a:
    if x%i == 0:
        print(i)