from collections import deque
import sys

N, M, K, X = map(int, sys.stdin.readline().split())

graph = []
for i in range(N+1):
    graph.append([])

for i in range(M):
    town, link = map(int, sys.stdin.readline().split())
    graph[town].append(link)

visited = [False] * (N+1)
answer = []

def bfs(x):
    queue = deque()
    queue.append((x, 0))

    while queue:
        v, cnt = queue.popleft()

        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append((i, cnt + 1))
        
        if cnt == K:
            answer.append(v)

bfs(X)

if len(answer) == 0:
    print(-1)
else:
    # answer.sort()
    for i in answer:
        print(i)