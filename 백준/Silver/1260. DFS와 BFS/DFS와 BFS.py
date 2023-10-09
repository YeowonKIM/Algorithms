def DFS(num):
    print(num,end=' ') 
    visited[num] = 1 
    for i in range(N+1):
        if visited[i]==0 and graph[num][i]==1:
            DFS(i)

def BFS(num):
    result = [num]
    visited[num] = 0 
    while(result):
        num = result[0]
        print(num,end=' ')
        del result[0]
        for i in range(N+1):
            if visited[i]==1 and graph[num][i]==1:
                result.append(i)
                visited[i]=0

import sys
N, M,V = map(int, sys.stdin.readline().split())

graph = [[0]*(N+1) for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
for i in range(M):
    a,b = map(int, sys.stdin.readline().split())
    graph[a][b] =1
    graph[b][a] =1

DFS(V)
print()
BFS(V)