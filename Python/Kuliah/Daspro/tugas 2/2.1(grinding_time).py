N = int(input())

Abyss_mage = int((N)//10)
Hilichurl = int(((N)%10)//8)
if ((((N)%10)%8)%6) > 0 :
    Slime = int(((((N)%10)%8)//6)+1)
elif ((((N)%10)%8)%6) == 0 :
    Slime = int((((N)%10)%8)//6)

a = int(Abyss_mage*5)
b = int(Hilichurl*4)
c = int(Slime*3)

print(a+b+c)
print(Slime)
print(Hilichurl)
print(Abyss_mage)