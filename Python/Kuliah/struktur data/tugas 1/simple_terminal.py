a = 1
wadah = []
    
while a == 1:
    x = list(map(str, input().split()))
    if x[0] == "stop":
        a = 0
    elif x[0] == "append":
        wadah.append(x[1])
    elif x[0] == "prepend":
        wadah.insert(0,x[1])
    elif x[0] == "cp":
        wadah.insert(int(x[2]), wadah[int(x[1])])
    elif x[0] == "mv":
        wadah.insert(int(x[2]), wadah.pop(int(x[1])))
    elif x[0] == "rm":
        wadah.pop(int(x[1]))

print(len(wadah))
for i in wadah:
    print(i)