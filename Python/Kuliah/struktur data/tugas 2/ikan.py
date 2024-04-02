a = int(input())
x = list(map(int, input().split()))
while x:
    stack = []
    for i, ikan in enumerate(x):
        stack.append(ikan)
        if ikan == max(x):
            break
    stack = sorted(stack)
    stack.reverse()
    idx = 0
    for i, nilai in enumerate(stack):
        if stack[i + 1] == stack[i] - 1:
            if i == len(stack) - 2:
                idx = len(stack) - 1
                break
        else:
            idx = i
            break
    for i in range((idx + 1), len(stack)):
        stack.pop()
    for i in stack:
        x.remove(i)
    for i, nilai in enumerate(stack):
        stack[i] = str(nilai)
    y = " ".join(stack)
    print(y)
