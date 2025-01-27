import random as rd
from collections import defaultdict
MAX_INT = 2147483647
__version__ = "1.0.6"
Built = defaultdict(bool)

# class TreeNode():
#   def __init__(self, state, up = None, down = None, right = None, left = None):
#     self.state = state
#     self.up = up
#     self.down = down
#     self.right = right
#     self.left = left
#   def __str__(self) -> str:
#     return self.state
   

def is_solvable(state):
  """
    Check if the given state is solvable.

    Args:
        state (str): A string representing the current state of the puzzle.

    Returns:
        bool: True if the state is solvable, False otherwise.
    """
  blank_index = state.index('0')
  if(blank_index == 8):
    return True
  else:
    return False
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
    if(Built["123804765"] or Built["123456780"])or Built['187206345']:
      Built["123804765"] = False
      Built["123456780"] = False
      Built['187206345'] = False
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
def build_graphW(graph , start_node):
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
  found = 0
  start  = graph[start_node]
  while(True):
    # build the graph level by level and stop when 123456780 found
    for child in start :
    
      graph[child] = get_children(child)
      if("123456780" in graph[child] ):
        found += 1
        for childs in graph[child] :
          graph[childs] = get_children(child)
    if found == 1:
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
    found = 0
    start = graph[start_node]
    while True:
        # build the graph level by level and stop when 123456780 found
        for child in start:
            graph[child] = get_children_UnWeighted(child)
            if ("123456780" in graph[child] or "187206345" in graph[child]or "123804765" in graph[child]):
                found += 1
                for childs in graph[child]:
                    graph[childs] = get_children_UnWeighted(child)
        if found == 1:
            break
        key += 1
        iterations += 1
        try:
            start = graph[list(graph.keys())[key]]
        except:
            break

    return graph
def GenerateRandStr()->str:
  """
    Generate a random solvable puzzle state.

    Returns:
        str: A string representing a solvable puzzle state.
  """
  while(True):
    st = list('123456780')
    visits = []
    i = 0
    while(i < 9):
      r = rd.randint(0,8)
      if(r not in visits):
        st[i] = str(r)
        i += 1
        visits.append(r)
    ans = "".join(st)
    if(is_solvable(ans)): 
      return ans
    else:
      pass
def build_WeightedGraph(graph: dict, costs: dict) -> dict:
    """
    Construct a weighted graph from the given graph and returns costs dictionary.

    Args:
        graph (dict): A dictionary representing the current state of the puzzle.
        costs (dict): An empty dictionary will containing the costs of each child node.

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
def BuildFull(initialState:str):
  '''
  return a tuple containing all the components of a weighted graph 
  -sample:"013425786"
  '''
  puzzle_state = initialState
  graph = {}
  costs = {}
  parents = {}
  graph = build_graphW(graph , puzzle_state )
  parents = build_ParentTree(graph , parents )    
  costs = build_WeightedGraph(graph, costs)
  return graph, parents, costs
def BuildFull_UnWeighted(initialState:str):
  '''
  return an unweighted graph
  '''
  puzzle_state = initialState
  graph = {}
  graph = buildGraph_UnWeighted(graph , puzzle_state )
  return graph

