a = 0
jawaban = []
while a == 0:
    x = input()
    if x == "stop":
        break
    x = [char for char in x]
    stack = []
    stack1 = []
    for i, char in enumerate(x):
        if char != "/":
            stack1.append(char)
            if i == len(x) - 1:
                break
        else:
            if not stack:
                continue
            ntah = "".join(stack1)
            stack.append(ntah)
    x = 0
    print(stack)
    stack1 = stack.copy()
    for i in stack:
        if i == ".":
            stack1.remove(i)
        elif i == "..":
            x -= 1
            stack1.remove(i)
        else:
            x = stack.index(i)
    print(stack)
    print(stack1)
    while len(stack1) > stack1.index(stack[x]):
        stack1.pop()
    ntah = "/".join(stack1)
    jawaban.append(ntah)
for i in jawaban:
    print(i)
