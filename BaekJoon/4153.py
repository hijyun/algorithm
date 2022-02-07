while True:
    a, b, c = list(map(int, input().split()))
    if a == 0 or b == 0 or c ==0:
        break

    if a > c:
        a, c = c, a
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b

    if a**2 + b**2 == c **2:
        print('right')
    else:
        print('wrong')