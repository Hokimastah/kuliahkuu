a, b = map(int,input().split())
c = []
matrix = []

for i in range(a):
    matrix.append(list(map(int, input().split())))


def pulau(a, b):
    if (
        a >= 0
        and a < len(matrix[0])
        and b >= 0
        and b < len(matrix)
        and matrix[a][b] == 1
    ):
        matrix[a][b] = 0
        size = 1
        size += pulau(a + 1, b)
        size += pulau(a - 1, b)
        size += pulau(a, b + 1)
        size += pulau(a, b - 1)

        return size
    return 0


for i in range(a):
    for j in range(b):
        if matrix[i][j] == 1:
            c.append(pulau(i, j))

d = len(c)
e = " ".join(map(str,c))
print(f"Banyak Pulau: {d}")
print(f"Luas Pulau: {e}")