import sys
a, b = map(int, sys.stdin.readline().split())
num = []

for i in range(1, b+1):
    for _ in range(i):
        num.append(i)
print(sum(num[a-1:b]))