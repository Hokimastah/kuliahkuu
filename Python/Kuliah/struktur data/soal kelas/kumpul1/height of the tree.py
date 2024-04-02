def makeNode(key):
    return {'key': key, 'left': None, 'right': None}
def Insert(root, value):
# compare keys and insert node into right place
    if not root:
        root = makeNode(value)
    elif value < root['key']:
        if not root['left']: root['left'] = makeNode(value)
        else: Insert(root['left'], value)
    elif value >= root['key']:
        if not root['right']: root['right'] = makeNode(value)
        else: Insert(root['right'], value)
    else: print("maaf node yang amda masukan sudah ada")

root = None
angkaMasukan = list(map(int,input().split()))
root = makeNode(angkaMasukan[0])

for angka in angkaMasukan[1:]:
    if angka == 0: break
    Insert(root, angka)


def leave(root,x,y):
    if root:
        x += 1
        leave(root['left'],x,y)
        x -= 1
        leave(root['right'],x,y)
    else: y.append(x)
 
x = 0
y = []
leave(root,x,y)
print(max(y))