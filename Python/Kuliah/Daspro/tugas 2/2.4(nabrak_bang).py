x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

if max(x1, x2) < min(x3, x4) or max(x3, x4) < min(x1, x2) or max(y1, y2) < min(y3, y4) or max(y3, y4) < min(y1, y2):
    print("gaspol bangg")
else:
    print("awas nabrak")