n = int(input())
a = n//250
b = (n%250)//100
c = ((n%250)%100)//50
d = (((n%250)%100)%50)//20
e = ((((n%250)%100)%50)%20)//10
f = (((((n%250)%100)%50)%20)%10)//5
# g
an = str(a)
bn = str(b)
cn = str(c)
dn = str(d)
en = str(e)
fn = str(f)

if n%5 !=0:
    print("Harganya jelek :(")
    StopIteration

print ( an + ' ' + 'lembar 250 ribuan')
print ( bn + ' ' + 'lembar 100 ribuan')
print ( cn + ' ' + 'lembar 50 ribuan')
print ( dn + ' ' + 'lembar 20 ribuan')
print ( en + ' ' + 'lembar 10 ribuan')
print ( fn + ' ' + 'lembar 5 ribuan')