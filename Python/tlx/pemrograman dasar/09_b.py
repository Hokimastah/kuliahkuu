x = []
while True:
    try:
        x.append(input())
    except:
        EOFError
        break

for i in range(len(x)-1):
    print(x[len(x)-1-i])