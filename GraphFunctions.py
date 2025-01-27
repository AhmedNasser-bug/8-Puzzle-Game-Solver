from math import inf
import numpy as np
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
        

def Representation2D(node:str):
    l = []
    c =0
    for rows in range(3):
        i = []
        for cols in range(3):
            i.append(int(node[c]))
            c+= 1
        l.append(i)
    return np.array(l)


