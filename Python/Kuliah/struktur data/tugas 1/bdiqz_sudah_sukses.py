a = 1
toko1 = []
toko2 = []

output = []

def t1():
    global toko1
    a = 1
    while a == 1:
        x = list(map(str,input().split()))
        if x[0] == "TUTUP":
            a+=1
        elif x[0] == "PESAN":
            y = [int(x[1]),int(x[2])]
            toko1.append(y)
        elif x[0] == "CURI":
            if len(toko1)>0: toko1.pop()
            if not toko1:
                output.append("TOKO 1 KOSONG")
        elif x[0] == "TUKAR":
            return t2()
def t2():
    global toko2
    a = 1
    while a == 1:
        x = list(map(str,input().split()))
        if x[0] == "TUTUP":
            a+=1
        elif x[0] == "PESAN":
            y = [int(x[1]),int(x[2])]
            toko2.append(y)
        elif x[0] == "CURI":
            if len(toko2)>0 : toko2.pop(0)
            if not toko2:
                output.append("TOKO 2 KOSONG")
        elif x[0] == "TUKAR":
            return t1()

t2()

for i in output:
    print(i)

print("TOKO 1 :")
untung = 0
if len(toko1)>0 :
    for i in toko1:
        print(f"{i[0]} {i[1]}")
        untung += int(i[1])
else: print("TOKO 1 SEPI : (")
    
print(f"TOKO 1 UNTUNG : {untung}")

print("TOKO 2 :")
untung = 0
if not toko1: print("TOKO 2 SEPI : (")
else :
    for i in toko2:
        print(f"{i[0]} {i[1]}")
        untung += int(i[1])
print(f"TOKO 2 UNTUNG : {untung}")