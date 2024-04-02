a, b = map(int, input().split())
arena = []
for i in range(a):
    x = input()
    y = [char for char in x]
    arena.append(y)

c = int(input())
d = input()
langkah = [char for char in d]

def arena2(a):
    for i in a:
        b = "".join(i)
        print(b)

def finish(a, b, c):
    a[b][c] = "*"
    arena2(a)
    print("Robot Mencapai Finish")
    return

step = 0

def jalan(arena, langkah, step, a, b):
    if langkah[step] == "w":
        step += 1
        if a >= 1 and a <= len(arena) and b >= 0 and b <= len(arena[0]):
            if arena[a - 1][b] == ".":
                arena[a - 1][b] = "#"
                return jalan(arena, langkah, step, a - 1, b)
            elif arena[a - 1][b] == "$":
                return finish(arena, a - 1, b)
            elif arena[a - 1][b] == "0":
                print(f"{step} Robot Menabrak Obstacle")
                return jalan(arena, langkah, step, a, b)
        else:
            print(f"{step} Robot Menabrak Tembok")
            return jalan(arena, langkah, step, a, b)

    elif langkah[step] == "d":
        step += 1
        if a >= 0 and a <= len(arena) and b >= 0 and b <= (len(arena[0]) - 1):
            if arena[a][b + 1] == ".":
                arena[a][b + 1] = "#"
                return jalan(arena, langkah, step, a, b + 1)
            elif arena[a][b + 1] == "$":
                return finish(arena, a, b + 1)
            elif arena[a][b + 1] == "0":
                print(f"{step} Robot Menabrak Obstacle")
                return jalan(arena, langkah, step, a, b)
        else:
            print(f"{step} Robot Menabrak Tembok")
            return jalan(arena, langkah, step, a, b)

    elif langkah[step] == "a":
        step += 1
        if a >= 0 and a <= len(arena) and b >= 1 and b <= len(arena[0]):
            if arena[a][b - 1] == ".":
                arena[a][b - 1] = "#"
                return jalan(arena, langkah, step, a, b - 1)
            elif arena[a][b - 1] == "$":
                return finish(arena, a, b - 1)
            elif arena[a][b - 1] == "0":
                print(f"{step} Robot Menabrak Obstacle")
                return jalan(arena, langkah, step, a, b)
        else:
            print(f"{step} Robot Menabrak Tembok")
            return jalan(arena, langkah, step, a, b)
    elif langkah[step] == "s":
        step += 1
        if a >= 0 and a <= (len(arena) - 1) and b >= 0 and b <= len(arena[0]):
            if arena[a + 1][b] == ".":
                arena[a + 1][b] = "#"
                return jalan(arena, langkah, step, a + 1, b)
            elif arena[a + 1][b] == "$":
                return finish(arena, a + 1, b)
            elif arena[a + 1][b] == "0":
                print(f"{step} Robot Menabrak Obstacle")
                return jalan(arena, langkah, step, a, b)
        else:
            print(f"{step} Robot Menabrak Tembok")
            return jalan(arena, langkah, step, a, b)


for i in range(a):
    for j in range(b):
        if arena[i][j] == "*":
            arena[i][j] = "#"
            jalan(arena, langkah, step, i, j)
            break
