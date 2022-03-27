from collections import deque
import sys
read = sys.stdin.readline

def dfs(graph, v, visited):
  # 현재 노드를 방문 처리
  visited[v] = True
  print(v, end = " ")

  # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)


def bfs(graph, v, visited):
  # 큐 구현을 위해 deque 라이브러리 사용
  q = deque()
  q.append(v)
  # 현재 노드를 방문 처리
  visited[v] = True

  while q: # 큐가 빌 때 까지 반복
    v = q.popleft()
    print(v, end = " ")
    # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
    for i in graph[v]:
      if not visited[i]:
        q.append(i)
        visited[i] = True

n, m, v = map(int, read().split())

graph = [[0] * (n + 1) for _ in range(n + 1)]
visit_dfs = [False] * (n + 1)
visit_bfs = [False] * (n + 1)

for _ in range(m):
  a, b = map(int, read().split())
  graph[a][b] = graph[b][a] = 1

dfs(graph, v, visit_dfs)
bfs(graph, v, visit_bfs)