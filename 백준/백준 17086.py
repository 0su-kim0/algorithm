from collections import deque

N,M = map(int,input().split())

graph=[]

for _ in range(N):
    graph.append(list(map(int,input().split())))
    
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]


def bfs(y,x):
    queue=deque()
    queue.append((y,x))

    visited=[[0] * M for _ in range(N)]
    visited[y][x]=1
    
    while queue:
        y,x= queue.popleft()
        
        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0 <= nx < M and 0 <= ny < N and visited[ny][nx] == 0:
                
                if graph[ny][nx]==1: #상어 발견시 거리반환
                    return visited[y][x] 
                else:
                    queue.append((ny,nx))
                    visited[ny][nx]=visited[y][x]+1
    return 0

ans = 0
for y in range(N):
    for x in range(M):
        if graph[y][x] != 1:  # 현재 위치가 아기 상어가 없는경우
            distance = bfs(y, x)  # 안전 거리 계산
            if ans < distance:  # 계산된 안전 거리와 비교 후 갱신
                ans = distance 

print(ans)