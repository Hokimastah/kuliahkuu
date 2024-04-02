a = list(input())
b = len(a) // 2
x = 0
for i in a:
    if a[x] == a.pop():
        x += 1
        if x == b:
            print("palindrom")
    else:
        print("bukan palindrom")
        break
