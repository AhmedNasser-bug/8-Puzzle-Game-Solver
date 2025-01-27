
import random
from collections import deque

def find_empty_space(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j
def get_successors(state):
    successors = []
    empty_index = state.index('0')
    empty_row, empty_col = empty_index // 3, empty_index % 3
    
    # Define all possible moves (up, down, left, right)
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    for dr, dc in moves:
        new_row, new_col = empty_row + dr, empty_col + dc
        
        # Check if the move is within the bounds of the puzzle
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_state = list(state)  # Convert the state string to a list to modify it
            new_index = new_row * 3 + new_col
            new_state[empty_index], new_state[new_index] = new_state[new_index], new_state[empty_index]
            successors.append((''.join(new_state), (dr, dc)))  # Convert list back to string
            
    return successors
def bfs(initial_state, goal_state):
    queue = deque([(initial_state, [])])  # Queue stores (state, path_to_state) pairs

    visited = set()  # Set to keep track of visited states
    
    while queue:
        state, path = queue.popleft()
        
        if state == goal_state:
            return path  # Return the path to the goal state
        
        visited.add(state)  # Mark the current state as visited
        
        # Generate all possible successor states
        successors = get_successors(state)  #num :[all possibilities ]
        
        for successor, move in successors:
            if successor not in visited:
                queue.append((successor, path + [move]))  # Add successor to the queue with updated path
                
    return "No solution"
def generate_random_state():
    # Create a list representing the puzzle grid
    puzzle_grid = list((range(1, 9))) + [0]  # zero represents the empty space
    
    # Shuffle the puzzle grid to create a random initial state
    random.shuffle(puzzle_grid)
    #[0,3,5,6,8,1,4,2,7]......>[0,3,5] , [6,8,1],[4,2,7]
    # Reshape the puzzle grid into a 3x3 matrix
    random_state = [puzzle_grid[i:i+3] for i in range(0, 9, 3)]
    random_state_flat = [str(num) if num is not None  else " " for row in random_state for num in row]
    return "".join(random_state_flat)

GoalPost="123456780"
while True:
    initial_state = generate_random_state()
    solution = bfs(initial_state, GoalPost)
    if solution != "No solution":
        print("Initial State:", initial_state)
        print("Solution Path:", solution)
        break




solution = bfs(generate_random_state(),GoalPost)
print(solution)