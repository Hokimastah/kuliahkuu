a = int(input())
x = list(range(1,a+1))
for i in x:
    if i == 42:
        print("ERROR")
        break
    elif i%10 == 0:
        continue
    else:
        print(i)