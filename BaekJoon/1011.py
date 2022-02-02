t = int(input())

for _ in range(t):
    x, y = map(int, input().split())

    tmp = 0
    cnt = 0
    moving = 0
    distance = y - x

    while tmp < distance:
        cnt += 1
        if cnt % 2 != 0:
            moving += 1
        tmp += moving
    print(cnt)