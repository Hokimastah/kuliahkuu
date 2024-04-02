n = int(input())
piring = []
hasil = []
        
for u in range(n):
    perintah = list(map(str,input().split()))
    if perintah[0] == "add":
        for i in range(int(perintah[2])):
            piring.append(int(perintah[1]))
        hasil.append(len(piring))
    elif perintah[0] == "del":
        hasil.append(piring[-1])
        for i in range(int(perintah[1])):
            piring.pop()
    elif perintah[0] == "adx":
        for i in range(len(piring)):
            piring[i] = piring[i]+int(perintah[1])
    elif perintah[0] == "dex":
        for i in range(len(piring)):
            piring[i] = piring[i]-int(perintah[1])
    elif perintah[0] == "mux":
        for i in range(len(piring)):
            piring[i] = piring[i]*int(perintah[1])
for i in hasil:
    print(i)