huruf = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
huruf2 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','X']
a = input()
x = [char for char in a]
b = int(input())
c = []
for i in x:
    if huruf.count(i) == 1:
        c.append(huruf[(huruf.index(i)+b)%26])
    elif huruf2.count(i) == 1:
        c.append(huruf2[(huruf2.index(i)+b)%26])
    else: c.append(i)

e = "".join(c)
print(e)