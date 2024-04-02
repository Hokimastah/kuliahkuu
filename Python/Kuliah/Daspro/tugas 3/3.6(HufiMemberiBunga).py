a = int(input())

b = []
for i in range (a):
    b.append(int(input()))

def palindrom(b):
    return str(b) == str(b)[::-1]

for c in b :
    if palindrom(c) :
        print('Mehas pasti suka!')
    else :
        print('Jangan ini, deh.')


