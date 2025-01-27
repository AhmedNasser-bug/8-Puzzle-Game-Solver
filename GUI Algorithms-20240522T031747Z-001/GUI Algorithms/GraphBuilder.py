import random as rd
import itertools
from collections import defaultdict
from GraphFunctions import Representation2D

MAX_INT = 2147483647
__version__ = "1.0.7"
Built = defaultdict(bool)
def getInvCount(arr):
	inv_count = 0
	empty_value = 0
	for i in range(0, 9):
		for j in range(i + 1, 9):
			if arr[j] != empty_value and arr[i] != empty_value and arr[i] > arr[j]:
				inv_count += 1
	return inv_count
def isSolvable(puzzle) :

	inv_count = getInvCount([j for sub in puzzle for j in sub])

	return (inv_count % 2 == 0)
def get_children(node):
  """
    Generate all possible child nodes from the given node.

    Args:
        node (str): A string representing the current state of the puzzle.

    Returns:
        dict: A dictionary containing all possible child nodes as keys and their corresponding costs as values.
  """
   
  global Built
  Built[node] = True
  children = {}
  StrBlank_Index = node.index('0')
  upAvailable:bool = False
  DownAvailable:bool  = False
  RightAvailable:bool  = True
  LeftAvailable:bool  = True
  
  if(StrBlank_Index in list(range(0 , 6))): upAvailable = True
  if(StrBlank_Index in list(range(3 ,9))):DownAvailable = True
  if(StrBlank_Index in [0 , 3 , 6]):RightAvailable = False
  if(StrBlank_Index in [2 , 5 , 8]):LeftAvailable = False
  # test if the move is available and add it to the children list
  if(upAvailable):
    child1 = list(node)
    next = node[StrBlank_Index + 3]
    child1[StrBlank_Index+ 3] , child1[StrBlank_Index] = node[StrBlank_Index],  next
    child1 = ''.join(child1)
    if(not Built[child1]):
      children[child1] = rd.randint(0,10)
      Built[child1] = True

  if(DownAvailable):
    child2 = list(node)
    next = node[StrBlank_Index - 3]
    child2[StrBlank_Index- 3] , child2[StrBlank_Index] = node[StrBlank_Index],  next
    child2 = str().join(child2)
    if(not Built[child2]):
      children[child2] = rd.randint(0,10)
      Built[child2] = True

  if(RightAvailable):
    child3 = list(node)
    next = child3[StrBlank_Index- 1] 
    child3[StrBlank_Index-1] , child3[StrBlank_Index] = node[StrBlank_Index], next
    child3 = str().join(child3)
    if(not Built[child3]):
      children[child3] = rd.randint(0,10)
      Built[child3] = True

  if(LeftAvailable):
    child4 = list(node)
    next = child4[StrBlank_Index+ 1] 
    child4[StrBlank_Index+ 1] , child4[StrBlank_Index] = node[StrBlank_Index], next
    child4 = str().join(child4)
    if(not Built[child4]):
      children[child4] = rd.randint(0,10)
      Built[child4] = True


  return children
def get_children_UnWeighted(node):
  global Built
  Built[node] = True
  children = []
  StrBlank_Index = node.index('0')
  upAvailable:bool = False
  DownAvailable:bool  = False
  RightAvailable:bool  = True
  LeftAvailable:bool  = True
  
  if(StrBlank_Index in list(range(0 , 6))): upAvailable = True
  if(StrBlank_Index in list(range(3 ,9))):DownAvailable = True
  if(StrBlank_Index in [0 , 3 , 6]):RightAvailable = False
  if(StrBlank_Index in [2 , 5 , 8]):LeftAvailable = False
  # test if the move is available and add it to the children list
  if(upAvailable):
    child1 = list(node)
    next = node[StrBlank_Index + 3]
    child1[StrBlank_Index+ 3] , child1[StrBlank_Index] = node[StrBlank_Index],  next
    child1 = ''.join(child1)
    if(not Built[child1]):
      children.append(child1)
      Built[child1] = True

  if(DownAvailable):
    child2 = list(node)
    next = node[StrBlank_Index - 3]
    child2[StrBlank_Index- 3] , child2[StrBlank_Index] = node[StrBlank_Index],  next
    child2 = str().join(child2)
    if(not Built[child2]):
      children.append(child2)
      Built[child2] = True

  if(RightAvailable):
    child3 = list(node)
    next = child3[StrBlank_Index- 1] 
    child3[StrBlank_Index-1] , child3[StrBlank_Index] = node[StrBlank_Index], next
    child3 = str().join(child3)
    if(not Built[child3]):
      children.append(child3)
      Built[child3] = True

  if(LeftAvailable):
    child4 = list(node)
    next = child4[StrBlank_Index+ 1] 
    child4[StrBlank_Index+ 1] , child4[StrBlank_Index] = node[StrBlank_Index], next
    child4 = str().join(child4)
    if(not Built[child4]):
      children.append(child4)
      Built[child4] = True


  return children
def build_graph(graph , start_node):
  """
    Generate a graph representing all possible states of the puzzle.

    Args:
        graph (dict): A dictionary representing the current state of the puzzle.
        start_node (str): A string representing the initial state of the puzzle.

    Returns:
        dict: A dictionary containing all possible child nodes as keys and their corresponding costs as values.
  """
  print("Generating graph......")
  graph[start_node] = get_children(start_node)
  key = 0
  iterations  = 1
  found = False
  start  = graph[start_node]
  while(True):
    # build the graph level by level and stop when 123456780 found
    for child in start :
    
      graph[child] = get_children(child)
      if("123456780" in graph[child]):
        found = True
        for childs in graph[child] :
          graph[childs] = get_children(child)
    if found:
      break
    key += 1
    iterations += 1
    try:
      start =graph[list(graph.keys())[key]]
    except:
      break
 
  return graph
def buildGraph_UnWeighted(graph, start_node):
    """
    Generate an unweighted graph representing all possible states of the puzzle.

    Args:
        graph (dict): An empty dictionary representing the current state of the puzzle.
        start_node (str): A string representing the initial state of the puzzle.

    Returns:
        dict: A dictionary containing all possible child nodes as keys and their corresponding child nodes as values.

    Raises:
        ValueError: If the given node is not found in the graph.

    Note:
        This function populates the graph with all possible child nodes of the given start_node. It stops when it finds the goal state "123456780".
    """
    print("Generating graph(Unweighted)......")
    graph[start_node] = get_children_UnWeighted(start_node)
    key = 0
    iterations = 1
    found = False
    start = graph[start_node]
    while True:
        # build the graph level by level and stop when 123456780 found
        for child in start:
            graph[child] = get_children_UnWeighted(child)
            if ("123456780" in graph[child]):
                found = True
                for childs in graph[child]:
                      graph[childs] = get_children_UnWeighted(child)
        if found:
            break
        key += 1
        iterations += 1
        try:
            start = graph[list(graph.keys())[key]]
        except:
            break

    return graph
def GenerateRandStr()->str:
    # Create a list representing the puzzle grid
    puzzle_grid = list(range(1, 9)) + [0]  # zero represents the empty space
    print(puzzle_grid)
    # Shuffle the puzzle grid to create a random initial state
    rd.shuffle(puzzle_grid)
    
    # Reshape the puzzle grid into a 3x3 matrix
    random_state ="".join([str(num) if num != 0 else '0' for num in puzzle_grid])
    while(not isSolvable(Representation2D(random_state))):
    # Create a list representing the puzzle grid
     puzzle_grid = list(range(1, 9)) + [0]  # zero represents the empty space
    
    # Shuffle the puzzle grid to create a random initial state
     rd.shuffle(puzzle_grid)
    
    # Reshape the puzzle grid into a 3x3 matrix
     random_state = "".join([str(num) if num != 0 else '0' for num in puzzle_grid])  
    return random_state
def build_WeightedGraph(graph: dict, costs: dict) -> dict:
    """
    Construct a weighted graph from the given graph and costs dictionary.

    Args:
        graph (dict): A dictionary representing the current state of the puzzle.
        costs (dict): An empty dictionary containing the costs of each child node.

    Returns:
        dict: A dictionary containing the costs of each node in the graph.

    Raises:
        ValueError: If the given node is not found in the graph.

    Note:
        This function first populates the costs dictionary with the costs of the children of the first node in the graph.
        Then, it populates the costs of the remaining nodes with the maximum integer value.
    """
    costs = {}
    steps = 0
    for cost in graph[list(graph.keys())[0]].keys():
        costs[cost] = graph[list(graph.keys())[0]][cost]
        steps += 1
    for node in list(graph.keys())[1 + steps:]:
        costs[node] = MAX_INT
    return costs
def get_parent(graph: dict, node: str) -> str:
  """
    Get the parent node of the given node in the graph.

    Args:
        graph (dict): A dictionary representing the current state of the puzzle.
        node (str): A string representing the current state of the puzzle.

    Returns:
        str: The parent node of the given node in the graph.
  """
  if node not in graph:
    raise ValueError(f"Node '{node}' not found in the graph")

  # Iterate through all nodes in the graph
  for parent, children in graph.items():
    if node in children:
      return parent  # Parent found

  return None  # Node not found as a child in any parent
def build_ParentTree(graph , parents):
  for node in list(graph.keys()):
    parents[node] = get_parent(graph, node)
  return parents
def BuildFull(initialState:str)-> tuple:
  '''
  return a tuple containing all the components of a weighted graph 
  sample:"013425786"
  '''
  puzzle_state = initialState
  graph = {}
  costs = {}
  parents = {}
  graph = build_graph(graph , puzzle_state )
  parents = build_ParentTree(graph , parents )    
  costs = build_WeightedGraph(graph, costs)
  return graph, parents, costs
def BuildFull_UnWeighted(initialState:str)-> dict:
  '''
  return an unweighted graph
  '''
  puzzle_state = initialState
  graph = {}
  graph = buildGraph_UnWeighted(graph , puzzle_state )
  return graph
