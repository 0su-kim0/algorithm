N, V, M = map(int,input().split())

graph=[]
for i in range(M):
    graph.append(list(map(int,input())))

visited = [False]*
def dfs(graph,V,visited)):
    visied[V]=True
    print(V,end= ' ')
    for i in graph[V]:
        dfs(graph,i,visited)


