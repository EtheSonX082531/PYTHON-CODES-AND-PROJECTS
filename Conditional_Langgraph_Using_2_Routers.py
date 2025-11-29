from typing import TypedDict
from langgraph.graph import StateGraph,START,END

class AgentState(TypedDict):
    number1:int
    number2:int
    operation1:str
    number3:int
    number4:int
    operation2:str
    ans1:int
    ans2:int


def add_node1(state:AgentState)->AgentState:
    state["ans1"]=state["number1"]+state["number2"]
    return state


def subtract_node1(state:AgentState)->AgentState:
    state["ans1"]=state["number1"]-state["number2"]
    return state

def router1(state:AgentState)-> str:
    if state["operation1"] == "+":
        return "addition_operation1"
    else:
        return "subtraction_operation1"

def add_node2(state:AgentState)->AgentState:
    state["ans2"]=state["number3"]+state["number4"]
    return state
   

def subtract_node2(state:AgentState)->AgentState:
    state["ans2"]=state["number3"]-state["number4"]
    return state  


def router2(state:AgentState)-> str:
    if state["operation2"] == "+":
        return "addition_operation2"
    else:
        return "subtraction_operation2"
    
graph = StateGraph(AgentState)

graph.add_node("add_node1",add_node1)
graph.add_node("subtract_node1",subtract_node1)
graph.add_node("router1", lambda state: state)


graph.add_node("add_node2",add_node2)
graph.add_node("subtract_node2",subtract_node2)
graph.add_node("router2", lambda state: state)

graph.add_edge(START,"router1")

graph.add_conditional_edges(
    "router1",
    router1,
    {
      #"Edges":"nodes_name"
       "addition_operation1":"add_node1",
       "subtraction_operation1":"subtract_node1"
    }
)


graph.add_edge("add_node1","router2")
graph.add_edge("subtract_node1","router2")

graph.add_conditional_edges(
    "router2",
    router2,
    {
      "addition_operation2":"add_node2",
      "subtraction_operation2":"subtract_node2"
    }
)


graph.add_edge("add_node2",END)
graph.add_edge("subtract_node2",END)

app=graph.compile()

initial_state=app.invoke({"number1":33,"number2":36,"operation1":"+","number3":75,"number4":144,"operation2":"-"})

print("After Starting The Graph:")
print(initial_state["ans1"])
print(initial_state["ans2"])




