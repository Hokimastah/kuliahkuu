a = int(input())
def faktorial(x):
    if x == 0 :
        return 1
    return x*faktorial(x-1)

b = list(map(int, list(str(faktorial(a)))))
b.reverse()

c = 0
for i in b :
    if i ==  0 :
        c+=1
    elif i != 0 :
        break

print(c)
if c %2 == 0 :
    print('Tuker dulu Rink!')
else : print('Gas pol rem blong, Rink!')