import sys
n, x = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

result = []

for i in range(n):
    if data[i] < x:
        print(data[i], end = ' ')