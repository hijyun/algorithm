# 풀이 1
import sys
n = int(input())
data = list(map(int, sys.stdin.readline().split()))

print(min(data),max(data))

# 풀이 2
import sys
n = int(input())
data = list(map(int, sys.stdin.readline().split()))
data.sort()
print(data[0], data[n-1])

# 풀이 3
import sys
n = int(input())
data = list(map(int, sys.stdin.readline().split()))
min_idx = 0
max_idx = 0

for i in range(n):
    if data[i] < data[min_idx]:
        min_idx = i
    if data[i] > data[max_idx]:
        max_idx = i
print(data[min_idx], data[max_idx])