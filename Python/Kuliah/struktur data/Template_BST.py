def makeNode(key):
    return {'key': key, 'left': None, 'right': None}

def Insert(root, value):
# compare keys and insert node into right place
    if not root:
        root = makeNode(value)
    elif value < root['key']:
        if not root['left']: root['left'] = makeNode(value)
        else: Insert(root['left'], value)
    else:
        if not root['right']: root['right'] = makeNode(value)
        else: Insert(root['right'], value)

def search(root, value):
    while root:
        if value > root['key']:
            root = root['right']
        elif value < root['key']:
            root = root['left']
        else:
            return root
    return None

def findMin(node):
    current = node
    while current and current['left']:
        current = current['left']
    return current

def remove(root, value):
    if root == None: return root
    
    if value < root['key']:
        root['left'] = remove(root['left'], value)
    elif value > root['key']:
        root['right'] = remove(root['right'], value)
    else:
        # kalau ini node yang ingin kita hapus
        if root['left'] == None:
            temp = root['right']
            root = None
            return temp
        elif root['right'] == None:
            temp = root['left']
            root = None
            return temp
        temp = findMin(root['right'])
        root['key'] = temp['key']
        root['right'] = remove(root['right'], temp['key'])
    return root
def find(root, value):
    temp = search(root, value)
    if temp == None:return False
    if temp['key'] == value: return True
    else: return False

def InOrder(root):
    if root:
        InOrder(root['left'])
        print(root['key'], end=' ')
        InOrder(root['right'])

def PreOrder(root):
    if root:
        print(root['key'], end=' ')
        PreOrder(root['left'])
        PreOrder(root['right'])

def PostOrder(root):
    if root:
        PostOrder(root['left'])
        PostOrder(root['right'])
        print(root['key'], end=' ')


# Driver code
root = None
angkaMasukan = [36, 16, 12, 33, 44, 41, 89, 95]
root = makeNode(angkaMasukan[0]) # root harus diisi dengan node pertama

for angka in angkaMasukan[1:]:
    Insert(root, angka)
    # print(root)

print("InOrder:")
InOrder(root)
print("\nPreOrder:")
PreOrder(root)
print("\nPostOrder:")
PostOrder(root)

print("\n\nSearch 33:", find(root, 33))

remove(root, 33)
print("InOrder:")
InOrder(root)
print("\nPreOrder:")
PreOrder(root)
print("\nPostOrder:")
PostOrder(root)
print("\n\nSearch 33:", find(root, 33))