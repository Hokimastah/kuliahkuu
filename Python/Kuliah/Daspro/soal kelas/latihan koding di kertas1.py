def kabisat(x):
    if x%400 ==0 :
        return True
    elif x%100 ==0 :
        return False
    elif x%4 ==0 :
        return True
    else : return False

a = input().replace(",", "").split()

bulan = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "Nopember", "December"]

b = bulan.index(a[0]) + 1

c = int(a[1])
d = int(a[2])
Day = 0

if b>1 :
    Day+=31
if kabisat(d) ==True and b>2 :
    Day+=29
elif kabisat(d) ==False and b>2 :
    Day+=28
if b>3 :
    Day+=31
if b>4 :
    Day+=30 
if b>5 :
    Day+=31
if b>6 :
    Day+=30 
if b>7 :
    Day+=31
if b>8 :
    Day+=31
if b>9 :
    Day+=30
if b>10 :
    Day+=31
if b>11 :
    Day+=30

total_Day = Day + c
print(total_Day) 