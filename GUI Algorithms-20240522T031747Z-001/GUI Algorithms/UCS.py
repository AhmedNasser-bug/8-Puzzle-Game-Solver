from math import inf
import GraphBuilder 
from GraphFunctions import Representation2D
import gui
__name__ = '_main_'

def closest_node(graph, visited):  #sample function used to get the closest node we dont actually iterate through the graph 
    closest_node = None
    min_cost = inf
    for node, cost in graph.items():
      if cost < min_cost and node not in visited:  
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
    print(" UCS path: ")
    i = len(path) -1
    while(i >=0):
        yield Representation2D(path[i])
        i -= 1
    print("Goal Found!!")

def UCS(graph, costs, parent):
    """
    This function implements the UCS's shortest path algorithm on the given graph and costs.

    Parameters:
    - graph (dict): A dictionary representing the graph, where keys are the nodes and values are dictionaries of neighbors and their respective costs.
    - costs (dict): A dictionary representing the initial costs of each node.
    - parent (dict): A dictionary that will store the parent of each node in the shortest path.

    Returns:
    None. The function updates the 'costs' and 'parent' dictionaries in-place.

    Raises:
    - ValueError: If the graph or costs dictionary is empty.

    Uses the 'closest_node' function to find the node with the lowest cost at each iteration.
    Updates the costs and parent dictionaries accordingly.
    """
    visited = set()
    closest_one = closest_node(costs, visited) # we use that function again with the target parameter (cost) and the visited now is a set w
    while closest_one:  # the while loop helps after iterating through all the costs so we can go through all the nodes
        cost = costs[closest_one]
        try:
            graph[closest_one] = graph[closest_one]
        except:
            break
        for neighbor, neighbor_cost in graph[closest_one].items():
            new_cost = graph[closest_one][neighbor] + cost #we take the node for ex o and iterate through its keys using neighbor and values using neighborcost
            if new_cost < costs.get(neighbor, inf): #get formula returns value of key
                costs[neighbor] = new_cost
                parent[neighbor] = closest_one
        visited.add(closest_one)
        closest_one = closest_node(costs, visited)


construct = GraphBuilder.BuildFull("871346520")
graph = construct[0]
costs = construct[2]
parent = construct[1]
visualize_graph(graph)
UCS(graph, costs, parent)
states = list(yield_path(parent, '123456780'))
gui.main(states)