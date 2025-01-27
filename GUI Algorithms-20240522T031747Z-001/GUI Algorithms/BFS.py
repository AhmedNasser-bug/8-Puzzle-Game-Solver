import random
from collections import deque
import tkinter as tk
from tkinter import messagebox

# BFS algorithm and helper functions

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
            successors.append(''.join(new_state))  # Convert list back to string
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
        successors = get_successors(state)
        
        for successor in successors:
            if successor not in visited:
                queue.append((successor, path + [successor]))  # Add successor to the queue with updated path
                
    return "No solution"

def generate_random_state():
    # Create a list representing the puzzle grid
    puzzle_grid = list(range(1, 9)) + [0]  # zero represents the empty space
    
    # Shuffle the puzzle grid to create a random initial state
    random.shuffle(puzzle_grid)
    
    # Reshape the puzzle grid into a 3x3 matrix
    random_state = [str(num) if num != 0 else '0' for num in puzzle_grid]
    return ''.join(random_state)

# GUI class
class EightPuzzleGUI:
    def __init__(self, root, states):
        self.root = root
        self.states = states
        self.current_state_index = 0

        self.root.title("8-Puzzle Solver")
        self.create_widgets()

    def create_widgets(self):
        self.grid_frame = tk.Frame(self.root)
        self.grid_frame.pack()

        self.labels = [[tk.Label(self.grid_frame, font=("Helvetica", 32), width=4, height=2, borderwidth=2, relief="groove")
                        for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                self.labels[i][j].grid(row=i, column=j)

        self.prev_button = tk.Button(self.root, text="Previous Move", command=self.previous_move)
        self.prev_button.pack(side=tk.LEFT)

        self.next_button = tk.Button(self.root, text="Next Move", command=self.next_move)
        self.next_button.pack(side=tk.RIGHT)

        self.update_grid(self.states[self.current_state_index])

    def update_grid(self, state):
        for i in range(3):
            for j in range(3):
                self.labels[i][j].config(text=state[i * 3 + j] if state[i * 3 + j] != '0' else '')

    def next_move(self):
        if self.current_state_index < len(self.states) - 1:
            self.current_state_index += 1
            self.update_grid(self.states[self.current_state_index])
        else:
            messagebox.showinfo("Info", "No more moves!")

    def previous_move(self):
        if self.current_state_index > 0:
            self.current_state_index -= 1
            self.update_grid(self.states[self.current_state_index])
        else:
            messagebox.showinfo("Info", "This is the first move!")


GoalPost = "123456780"
while True:
    initial_state = "724105368"
    solution_path = bfs(initial_state, GoalPost)
    if solution_path != "No solution":
        print("Initial State:", initial_state)
        print("Solution Path:", solution_path)
        states = [initial_state] + solution_path
        break


root = tk.Tk()
app = EightPuzzleGUI(root, states)
root.mainloop()
