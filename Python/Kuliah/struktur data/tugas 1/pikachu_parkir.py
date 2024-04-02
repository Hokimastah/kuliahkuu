tes = int(input())
jawab = []
for i in range(tes):
    jam, slot = map(int,input().split())
    j = int(input())
    for k in range(j):
        a, b = map(int,input().split())
        if jam >= a and jam < b:
            slot -= 1
    if slot > 0: 
        jawab.append("Pika Pika!")
    else : 
        jawab.append("Pika Zzz")

for i in jawab:
    print(i)