import tkinter as tk
from collections import deque

step = ["Down", "Up", "Right", "Left"]
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def BFS(graph, s_x, s_y, g_x, g_y):
    global found
    found = False
    queue = deque()
    queue.append((s_x, s_y, 0))
    while queue:
        s_x, s_y, depth = queue.popleft()
        for i, (x, y) in enumerate(dir):
            n_x = s_x + x
            n_y = s_y + y
            if (n_x in range(len(graph)) and n_y in range(len(graph)) and graph[n_x][n_y] == 1):
                text_area.insert(tk.END, f"Moving {step[i]} --> ({n_x},{n_y})\n")
                if n_x == g_x and n_y == g_y:
                    text_area.insert(tk.END, "Goal found!\n")
                    text_area.insert(tk.END, f"Number of moves required : {depth + 1}\n")
                    found = True
                    return
                graph[n_x][n_y] = 0
                queue.append((n_x, n_y, depth + 1))

    if not found:
        text_area.insert(tk.END, "Goal can't be reached from the source!\n")

def submit():
    graph = []
    grid = int(grid_entry.get())
    text_area.delete(1.0, tk.END)
    text_area.insert(tk.END, "Enter the adjacency matrix:\n")
    for i in range(grid):
        row = list(map(int, matrix_entries[i].get().split()))
        graph.append(row)
    s_x, s_y = map(int, source_entry.get().split())
    g_x, g_y = map(int, goal_entry.get().split())
    BFS(graph, s_x, s_y, g_x, g_y)

# GUI Setup
root = tk.Tk()
root.title("BFS Pathfinding")

# Grid size input
grid_label = tk.Label(root, text="Enter the size of the grid:")
grid_label.grid(row=0, column=0, sticky="w")
grid_entry = tk.Entry(root)
grid_entry.grid(row=0, column=1, padx=5, pady=5)

# Adjacency Matrix inputs
matrix_entries = []
for i in range(5):  # Assuming maximum grid size of 5 for simplicity
    entry = tk.Entry(root)
    entry.grid(row=i + 1, column=1, padx=5, pady=2)
    matrix_entries.append(entry)

# Source and Goal inputs
source_label = tk.Label(root, text="Enter source co-ordinates (x y):")
source_label.grid(row=6, column=0, sticky="w")
source_entry = tk.Entry(root)
source_entry.grid(row=6, column=1, padx=5, pady=5)

goal_label = tk.Label(root, text="Enter goal co-ordinates (x y):")
goal_label.grid(row=7, column=0, sticky="w")
goal_entry = tk.Entry(root)
goal_entry.grid(row=7, column=1, padx=5, pady=5)

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.grid(row=8, columnspan=2, pady=10)

# Output text area
text_area = tk.Text(root, height=10, width=40)
text_area.grid(row=9, columnspan=2, pady=10)

root.mainloop()
