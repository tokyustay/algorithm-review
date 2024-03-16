def dfs(graph, v, visited) :
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i , visited)




graphExample = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,8,6],
    [1,7]
]

visited = [False] * 9

dfs(graphExample, 1, visited)