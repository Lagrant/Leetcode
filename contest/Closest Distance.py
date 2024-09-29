import math
cases = int(input())
for case in range(cases):
    x0, y0, x1, y1, x2, y2, x3, y3 = map(int, input().split(' '))
    A = x0 - x2
    B = x1 - x0 - x3 + x2
    C = y0 - y2
    D = y1 - y0 - y3 + y2
    a = D**2 + B**2
    b = 2 * (A * B + C * D)
    c = A**2 + C**2
    k = -b / (2. * a)
    if k < 0 or k > 1:
        value = min(c, a + b + c)
    else:
        value = a * k**2 + b * k + c
    print(f'Case {case + 1}: {math.sqrt(value)}')