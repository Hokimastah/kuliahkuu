s = [char for char in input()]

def sc(x):
    besar = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    kecil = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    z = x
    idx = 0
    for i in z:
        if i == '_':
            x[idx+1] = besar[kecil.index(x[idx+1])]
        idx += 1
    x = "".join(x)
    return x.replace('_','')

def cs(x):
    besar = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    kecil = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    z = x
    idx = 0
    for i in z:
        if besar.count(i) == 1:
            x[x.index(i)] = kecil[besar.index(i)]
            x.insert(idx,'_')
        idx += 1
    x = "".join(x)
    return(x)

if s.count('_') >=1:
    print(sc(s))
else:
    print(cs(s))