graph={
    5:[3,7],
    3:[2,4],
    7:[8],
    2:[],
    4:[8],
    8:[]
 }
 
visited=[]
queue=[]
 
def bfs(graph,visited,node):
    if node not in visited:
        visited.append(node)
        queue.append(node)
        while queue:
            m=queue.pop(0)
            print(m,end=", ")
            for child in graph[m]:
                if child not in visited:
                    visited.append(child)
                    queue.append(child)
            
print("Breadth first search")
bfs(graph,visited,5)
