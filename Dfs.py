graph = {
    0:[1,2],
    1:[2],
    2:[3,4],
    3:[],
    4:[]
}

visited = []

def dfs(node):
    if node not in visited:
        visited.append(node)
        for child in graph[node]:
            dfs(child)

dfs(0)   

print(visited)           
    
