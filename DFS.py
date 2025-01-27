import GraphBuilder
from GraphFunctions import Representation2D
graph = GraphBuilder.buildGraph_UnWeighted({} , "013425786")
goal = "123456780"
visited = set()
def DFS(Graph , goal , neighbor , errors = 0):
        global visited
        if neighbor not in visited:
            print(Representation2D(neighbor))
            print(" |\n\/")
            visited.add(neighbor)
    
        try:
         for node in Graph[neighbor]:
            if goal  in visited: 
                break
            
            else:
                return DFS(Graph, goal , node , errors)#Goes through all the children of a node in the graph
        except:
         for node in Graph[list(Graph.keys())[list(Graph.keys()).index(neighbor)+errors]]:
            if goal  in visited:
                print("Goal Found!") 
                break
            
            else:
                errors += 1
                return DFS(Graph, goal , node , errors) #Goes through all the children of a node in the graph
            
DFS(graph, goal , list(graph.keys())[0])
