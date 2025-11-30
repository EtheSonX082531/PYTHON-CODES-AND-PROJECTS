from typing import TypedDict
from langgraph.graph import StateGraph, START, END

# -------------------------
# Define state
# -------------------------
class AgentState(TypedDict):
    number1: int
    number2: int
    operation1: str
    number3: int
    number4: int
    operation2: str
    ans1: int
    ans2: int

# -------------------------
# Node functions
# -------------------------
def add_node1(state: AgentState) -> AgentState:
    state["ans1"] = state["number1"] + state["number2"]
    return state

def subtract_node1(state: AgentState) -> AgentState:
    state["ans1"] = state["number1"] - state["number2"]
    return state

def add_node2(state: AgentState) -> AgentState:
    state["ans2"] = state["number3"] + state["number4"]
    return state

def subtract_node2(state: AgentState) -> AgentState:
    state["ans2"] = state["number3"] - state["number4"]
    return state

# -------------------------
# Router functions
# -------------------------
def router1(state: AgentState) -> str:
    if state["operation1"] == "+":
        return "addition_operation1"
    else:
        return "subtraction_operation1"

def router2(state: AgentState) -> str:
    if state["operation2"] == "+":
        return "addition_operation2"
    else:
        return "subtraction_operation2"

# -------------------------
# Build the graph
# -------------------------
graph = StateGraph(AgentState)

# Add nodes
graph.add_node("add_node1", add_node1)
graph.add_node("subtract_node1", subtract_node1)
graph.add_node("add_node2", add_node2)
graph.add_node("subtract_node2", subtract_node2)

# Connect START to router1
graph.add_edge(START, "router1")

# Conditional edges for router1
graph.add_conditional_edges(
    "router1",
    router1,
    {
        "addition_operation1": "add_node1",
        "subtraction_operation1": "subtract_node1"
    }
)

# Connect first operation nodes to router2
graph.add_edge("add_node1", "router2")
graph.add_edge("subtract_node1", "router2")

# Conditional edges for router2
graph.add_conditional_edges(
    "router2",
    router2,
    {
        "addition_operation2": "add_node2",
        "subtraction_operation2": "subtract_node2"
    }
)

# Connect second operation nodes to END
graph.add_edge("add_node2", END)
graph.add_edge("subtract_node2", END)

# Compile the graph
app = graph.compile()

# -------------------------
# Invoke the graph
# -------------------------
initial_state = app.invoke({
    "number1": 33,
    "number2": 36,
    "operation1": "+",
    "number3": 75,
    "number4": 144,
    "operation2": "-"
})

# Print results
print("After Starting The Graph:")
print("ans1 =", initial_state["ans1"])
print("ans2 =", initial_state["ans2"])
