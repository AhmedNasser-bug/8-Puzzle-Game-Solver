import tkinter as tk
from tkinter import messagebox
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
                self.labels[i][j].config(text=str(state[i][j]) if state[i][j] != 0 else '')

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

def main(states):
        root = tk.Tk()
        app = EightPuzzleGUI(root, states)
        root.mainloop()