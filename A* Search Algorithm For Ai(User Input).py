#f(n)=g(n)+h(n)
import queue


def A_Star_Search(graph,h,start,goal):
    frontier=queue.PriorityQueue()
    f=h.get(start,float('inf'))
    frontier.put((f,start,[start],0))
    explored=set()
    while frontier.qsize():
        f,node,path,g=frontier.get()
        
        if(node==goal):
            return path,g
        
        if node in explored:
            continue
        
        explored.add(node)
        
        for neighbour,step_cost in graph[node].items():
            if neighbour not in explored:
                new_g=g+step_cost
                f=new_g+h.get(neighbour,float('inf'))
                frontier.put((f,neighbour,path+[neighbour],new_g))
    
    return None,float('inf')        


graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 3, 'E': 5},
    'C': {'E': 8},
    'D': {'G': 1},
    'E': {'G': 2},
    'G': {}
}

h = {
    'A': 10,
    'B': 6,
    'C': 7,
    'D': 3,
    'E': 2,
    'G': 0
}

print("--- A* Search ---")
start=input("Enter Starting Node:")
goal=input("Enter Goal Node:")

path,cost=A_Star_Search(graph,h,start,goal)
print("Path:",path)
print("Cost:",cost)
