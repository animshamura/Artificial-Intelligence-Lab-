# Author - Shamura Ahamd
import tkinter as tk
step = ["down", "up", "right", "left"]

def DFS(graph, s_x, s_y, g_x, g_y, depth):
    global found
    found = False
    graph[s_x][s_y] = 0
    for i in range(4):
        n_x = s_x + (((-1) ** (i % 2)) if i < 2 else 0)
        n_y = s_y + (((-1) ** (i % 2)) if i > 1 else 0)
        if (n_x in range(len(graph)) and n_y in range(len(graph)) and graph[n_x][n_y] == 1):
            depth += 1
            print(f"Moving {step[i]} to ({n_x}, {n_y})")
            if (n_x == g_x and n_y == g_y):
                print("Goal found!")
                print(f"Number of moves required: {depth}")
                found = True
                return
            else:
                DFS(graph, n_x, n_y, g_x, g_y, depth)
        if found:
            return

def submit():
    grid_size = int(grid_entry.get())
    graph = []
    print("Enter the adjacency matrix:")
    for i in range(grid_size):
        graph.append(list(map(int, matrix_entries[i].get().split())))
    s_x, s_y = map(int, source_entry.get().split())
    g_x, g_y = map(int, goal_entry.get().split())
    DFS(graph, s_x, s_y, g_x, g_y, 0)
    if not found:
        text_area.config(state=tk.NORMAL)
        text_area.insert(tk.END, "Goal can't be reached from the source!\n")
        text_area.config(state=tk.DISABLED)

# GUI Setup
root = tk.Tk()
root.title("DFS Pathfinding")

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
text_area.config(state=tk.DISABLED)

root.mainloop()
