a1, a2 = map(int, input().split())
x, y, xl, yl = map(int, input().split())
xs, ys = map(int, input().split())

import math

lw = x - (xl / 2)
lk = x + (xl / 2)
pw = y - (yl / 2)
pk = y + (yl / 2)

if xs >= lw and xs <= lk and ys >= pw and ys <= pk:
    print("KAMU SUDAH SAMPAI")
else:
    jx = abs(xs - x)
    jy = abs(ys - y)
    jarak = math.sqrt((jx * jx) + (jy * jy))
    print(f"{jarak:.2f} METER LAGI")
