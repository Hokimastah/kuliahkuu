n = int(input())
piring = []
hasil = []
def add(x,y):
    for i in range(y):
        piring.append(x)
    hasil.append(len(piring))
    
def dele(y):
    hasil.append(piring[-1])
    for i in range(y):
        piring.pop()
        
def adx(x):
    for i in range(len(piring)):
        piring[i] = piring[i]+x
        
def mux(x) :
    for i in range(len(piring)):
        piring[i] = piring[i]*x
        
def dex(x) :
    for i in range(len(piring)):
        piring[i] = piring[i]-x
        
for i in range(n):
    perintah = list(map(str,input().split()))
    if perintah[0] == "add":
        add(int(perintah[1]),int(perintah[2]))
    elif perintah[0] == "del":
        dele(int(perintah[1]))
    elif perintah[0] == "adx":
        adx(int(perintah[1]))
    elif perintah[0] == "dex":
        dex(int(perintah[1]))
    elif perintah[0] == "mux":
        mux(int(perintah[1]))
for i in hasil:
    print(i)