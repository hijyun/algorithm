from collections import deque
t = int(input())
for _ in range(t):
    n , x = map(int,input().split())
    que = deque(list(map(int,input().split())))
    idx_que = deque(list(range(n)))
    cnt = 0 # 몇번째인지 카운트
    while que:
        if que[0] == max(que): # 최대값일 경우 pop
            cnt += 1
            que.popleft()
            if idx_que.popleft() == x:
                print(cnt)
        else:
            que.append(que.popleft())
            idx_que.append(idx_que.popleft())

