import queue

def UCS(graph,start,goal):
    explored=set()
    frontier=queue.PriorityQueue()
    frontier.put((0,start,[start]))
    
    while(frontier.qsize()):
        cost,node,path=frontier.get()
        if(node==goal):
            return path,cost
        
        if node in explored:
            continue   
         
        explored.add(node)
        for neighbour,step_cost in graph[node].items():
            if neighbour not in explored:
                total_cost=cost+step_cost
                frontier.put((total_cost,neighbour,path+[neighbour]))     
    
    return None,float('inf')


graph = {
    'A': {'C': 4, 'B': 1},
    'B': {'D': 2, 'E': 5, 'A': 1},
    'C': {'F': 3, 'A': 4},
    'D': {'B': 2},
    'E': {'F': 1, 'B': 5},
    'F': {'E': 1, 'C': 3}
}

print("--- Uniform Cost Search User Input ---")
start=input("Enter Starting Node:")
goal=input("Enter Goal Node:")

path,cost=UCS(graph,start,goal)
print("Path is:",path)
print("Cost is:",cost)
