import sys

n = int(input())
data = list(map(int, sys.stdin.readline().split()))

print(sum(data)*(100/max(data))/n)