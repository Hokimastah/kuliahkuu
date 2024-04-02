a = int(input())
def kocak(x,y):
    if x%4 == 0 :
        x//=4
        y.append(x) 
    elif x>1 :
        x+=1
        y.append(x)
    else: return y
    return kocak(x,y)

print(kocak(a, [a]))

    
