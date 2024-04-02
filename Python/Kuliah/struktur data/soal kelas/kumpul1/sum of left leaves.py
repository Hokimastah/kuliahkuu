a = int(input())

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
    Insert(root, angka)


def leave(root,x):
    if root:
        x = root['key']
        leave(root['left'],x)
        leave(root['right'],x)
    else:
        if x > root['key']:
            print(root['key'])
x = 0
leave(root,x)