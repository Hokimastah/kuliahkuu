def floodfill(matrix,a,b,c,d,e):
    if matrix[a][b] == 1 or matrix[a][b] == 0:  
        if matrix[a][b] == 1:
            matrix[a][b] = -1
            c+=1
            
        elif matrix[a][b] == 0:
            matrix[a][b] == -1
            return
            
        
        if a >= 0 and b>=0 and a<=len(matrix) and b<=len(matrix[0]):
            floodfill(matrix,a-1,b,c,d,e)
            floodfill(matrix,a+1,b,c,d,e)
            floodfill(matrix,a,b-1,c,d,e)
            floodfill(matrix,a,b+1,c,d,e)
        d.append(len(c))
        c = []
        e += 1
        return d

w = list(map(int,input().split()))
a = w[0]
b = w[1]

matrix = []
for i in range(a):
    matrix.append(list(map(int,input().split())))
a-=1
b-=1

c = []
d = []
e = 0

floodfill(matrix,a,b,c,d,e)
print(d)