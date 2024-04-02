def makeNode(key):
    return {'key': key, 'left': None, 'right': None}

def Insert(root, value):
# compare keys and insert node into right place
    if not root:
        root = makeNode(value)
    elif value < root['key']:
        if not root['left']: root['left'] = makeNode(value)
        else: Insert(root['left'], value)
    elif value > root['key']:
        if not root['right']: root['right'] = makeNode(value)
        else: Insert(root['right'], value)
    else: print("maaf node yang amda masukan sudah ada")

def search(root, value):
    while root:
        if value > root['key']:
            root = root['right']
        elif value < root['key']:
            root = root['left']
        elif value == root['key']:
            return root
        else:
            break
            return None

def findMin(node):
    current = node
    while current and current['left']:
        current = current['left']
    return current

def findMax(node):
    current = node
    while current and current['right']:
        current = current['right']
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

root = None
angkaMasukan = list(map(int,input().split()))
root = makeNode(angkaMasukan[0]) # root harus diisi dengan node pertama

for angka in angkaMasukan[1:]:
    Insert(root, angka)

while root:
    command = list(map(str,input().split()))
    if command[0] == "search":
        print(f"search {command[1]}: {find(root,int(command[1]))}")
    elif command[0] == "insert":
        Insert(root,int(command[1]))
    elif command[0] == "remove":
        if find(root,command[1]) == True:
            print("okayy")
        else: print("node tidak ditemukan")
    elif command[0] == "FindMin":
        print(f"nilai minimumnya adalah: {findMin(root)}")
    elif command[0] == "FindMax":
        print(f"nilai maksimumnya adalah: {findMax(root)}")
    elif command[0] == "inOrder":
        InOrder(root)
    elif command[0] == "PostOrder":
        PostOrder(root)
    elif command[0] == "PreOrder":
        PreOrder(root)
    elif command[0] == "stop":
        break
    else :
        print("maaf perintah yang anda berikan salah")
        break