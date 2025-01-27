import numpy as np
from math import inf
import GraphBuilder
from GraphFunctions import Representation2D
import gui

def manhattan_distance(state, cost) -> dict:
    """
    Calculate the Manhattan distance heuristic for each node in the given state representation.

    Args:
    - state (dict): The state representation containing nodes and their connections.
    - cost (dict): The current cost for each node.
    - visited (set): The set of visited nodes.
    - closest_one (str): The closest node based on the current cost.

    Returns:
    - dict: A dictionary containing the Manhattan distance for each node.
    """
    distance_dict = {}
    
    # Define the goal state
    goal_state = np.array([[1, 2, 3],
                           [4, 5, 6],
                           [7, 8, 0]])  # 0 represents the empty tile

    # Loop through each node in the state representation
    for parent, children in state.items():
        # Convert the string representation of the parent to a 3x3 grid array
        parent_ar = np.array([[int(parent[i*3 + j]) for j in range(3)] for i in range(3)])
        
        parent_manhattan_distance = 0
        # Loop through each tile in the parent node
        for i in range(3):
            for j in range(3):
                value = parent_ar[i][j]
                if value != 0:
                    # Find the position of the value in the goal state
                    goal_i, goal_j = np.where(goal_state == value)
                    # Calculate the Manhattan distance
                    parent_manhattan_distance += abs(i - goal_i) + abs(j - goal_j)
        
        # Calculate the new cost with Manhattan distance heuristic
        try: # Check if the node is in the dictionary
            new_cost = cost[parent] + parent_manhattan_distance
        except :
            new_cost =  parent_manhattan_distance
        # Add the Manhattan distance to the dictionary for this node
        distance_dict[parent] = int(new_cost[0])
    
    return distance_dict

def closest_node(graph, visited , heuristic):  
    '''
     function used to get the closest node we dont actually iterate through the graph 
    '''
    closest_node = None
    min_cost = inf
    for node, cost in graph.items():
     if cost < min_cost and node not in visited: 
             try: 
                min_cost = cost + heuristic[node]
             except :
                 min_cost = cost
             closest_node = node  # with that logic the node with the lowest cost becomes the closest node
     return closest_node

def visualize_graph(graph):
     for node, neighbors in graph.items():    # o:j:1   o is the node and j is the neighbor and so forth in the iteration process 
         print(f"{node} --> ", end="")
         for neighbor, cost in neighbors.items():  # j:1    j is the nighbor and the cost is the 1 
             print(f"{neighbor} : {cost} ", end="")
         print()

def yield_path(parent, final_node):
    if final_node not in parent:
        print(f"No path found from first node to {final_node}")
        return

    # Reconstruct the path by following the parent nodes
    path = [final_node]
    current_node = final_node
    while current_node in parent:
        current_node = parent[current_node]
        path.append(current_node)
    path.pop(-1)#Remove the None value at the end of the path
    # Print the path in reverse order (final node to first node)
    print("A* path: ")
    i = len(path) -1
    while(i >=0):
        yield Representation2D(path[i])
        i -= 1
    print("Goal Found!!")

def A_star(graph, costs, parent , heuristic):
    visited = set()
    closest_one = closest_node(costs, visited , heuristic) # we use that function again with the target parameter (cost) and the visited now is a set w
    while closest_one:  # the while loop helps after iterating through all the costs so we can go through all the nodes
        cost = costs[closest_one]
        try:
            graph[closest_one] = graph[closest_one]
        except:
            break
        for neighbor, neighbor_cost in graph[closest_one].items():
            try:
                new_cost = graph[closest_one][neighbor] + cost + heuristic[neighbor] #we take the node for ex o and iterate through its keys using neighbor and values using neighbor cost
            except :
                 new_cost = graph[closest_one][neighbor] + cost
            if new_cost < costs.get(neighbor, inf): #get formula returns value of key
                costs[neighbor] = new_cost 
                parent[neighbor] = closest_one
        visited.add(closest_one)
        closest_one = closest_node(costs, visited , heuristic)
newFull = GraphBuilder.BuildFull("023451867")
costs = newFull[2]
Parents = newFull[1]
WeightedGraph = newFull[0]
heuristic = manhattan_distance(Parents, WeightedGraph)
A_star(WeightedGraph , costs , Parents, heuristic)
visualize_graph(WeightedGraph)
states = list(yield_path(Parents , '123456780'))
gui.main(states)

