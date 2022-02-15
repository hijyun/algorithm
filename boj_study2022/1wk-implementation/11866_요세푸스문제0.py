from collections import deque
n, k = map(int, input().split())
queue = deque(list(range(1, n+1)))

print('<', end='')

while queue:
    for r in range(k-1):
        queue.append(queue.popleft())
    print(queue.popleft(), end='')

    if queue:
        print(',', end=' ')

print('>')