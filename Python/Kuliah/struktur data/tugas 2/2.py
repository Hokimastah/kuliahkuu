page = list(map(str,input().split()))
page.insert(0,"Homepage")
di = 0
ntah = 1
while ntah == 1:
    x, y = map(str,input().split())
    if x != "visit":
        y = int(y)
    if x == "visit":
        di = page.index(y)
    elif x == "back":
        di-=y
        if di < 0:
            print("Waduh bang kayanya kamu salah input")
            break
    elif x == "forward":
        di+=y
        if di > len(page):
            print("Waduh bang kayaknya kamu salah input")
    else : print("Ga paham maksud lo gua bang :(")
    
    print(f"Abangku sekarang ladi di {page[di]}")