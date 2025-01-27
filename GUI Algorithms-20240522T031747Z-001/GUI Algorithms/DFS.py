import GraphBuilder
from GraphFunctions import Representation2D
import gui
graph = GraphBuilder.buildGraph_UnWeighted({} , "013425786")
goal = "123456780"
visited = set()
states = []
def get_move(current_state, next_state):
  """
  Determines the move (action) taken to get from the current state to the next state.

  Args:
      current_state (str): The current state of the puzzle as a string.
      next_state (str): The next state of the puzzle as a string.

  Returns:
      str: The move description (e.g., "Up", "Down", "Left", "Right")
  """

  # Find the position of the blank tile in both states
  blank_pos_current = current_state.find('0')
  blank_pos_next = next_state.find('0')

  # Calculate the difference in position (row and column)
  row_diff = blank_pos_next // 3 - blank_pos_current // 3
  col_diff = blank_pos_next % 3 - blank_pos_current % 3

  # Determine the move based on the difference
  if row_diff == -1:
      return "Up"
  elif row_diff == 1:
      return "Down"
  elif col_diff == -1:
      return "Left"
  elif col_diff == 1:
      return "Right"
  else:
      raise ValueError("Invalid state transition: Blank tile didn't move!")

def DFS(graph, current_state, goal_state, visited=None):
    """
    Performs Depth-First Search (DFS) for the 8-puzzle game.

    Args:
        graph (dict): A dictionary representing the graph, where keys are states and values are lists of reachable states.
        current_state (str): The current state of the puzzle as a string.
        goal_state (str): The goal state of the puzzle as a string.
        visited (set, optional): A set to store visited states to avoid cycles. Defaults to None.

    Returns:
        list or None: A list of moves (actions) leading to the goal state if found, or None otherwise.
    """

    if visited is None:
        visited = []

    if current_state == goal_state:
        # Goal reached! Return an empty list representing the starting state

        return []
    print(Representation2D(current_state) , end= "\n")
    states.append(Representation2D(current_state))
    visited.append(current_state)
    ErrorPossible = True
    try:
        for next_state in graph[current_state]:
            if next_state not in visited:
                path = DFS(graph, next_state, goal_state, visited.copy() )
                if path is not None:
                # Successful path found, prepend the current move to it (determine move using get_move)
                    return [get_move(current_state, next_state)] + path
    except:
        while(ErrorPossible):
         for k in range(len(list(graph.keys()))):
                current_state = visited[-1 - k]
                for i in graph[current_state]:
                    if(i not in visited):
                        ErrorPossible = False
        for next_state in graph[current_state]:
            if next_state not in visited:
                path = DFS(graph, next_state, goal_state, visited.copy())
                if path is not None:
                # Successful path found, prepend the current move to it (determine move using get_move)
                    return [get_move(current_state, next_state)] + path    

print(DFS(graph, list(graph.keys())[0] , goal))

gui.main(states)