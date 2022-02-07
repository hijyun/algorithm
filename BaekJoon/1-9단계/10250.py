import math
t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())
    if n % h == 0:
        print(h * 100 + math.ceil(n / h))
    else:
        print(n % h * 100 + math.ceil(n / h))

# 처음에 n % h ==0 인 경우를 처음에 처리 안해서 틀림.
# 나누기 있을 땐 0 되는 경우 체크하기.