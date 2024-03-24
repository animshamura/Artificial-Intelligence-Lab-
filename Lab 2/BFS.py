# Author - Shamura Ahmad
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
            if( n_x in range(len(graph)) and n_y in range(len(graph)) and graph[n_x][n_y]==1):
                print(f"Moving {step[i]} --> ({n_x},{n_y})")
                if n_x == g_x and n_y == g_y:
                    print("Goal found!")
                    print(f"Number of moves required : {depth + 1}")
                    found = True
                    return
                graph[n_x][n_y] = 0
                queue.append((n_x, n_y, depth + 1))

    if not found:
        print("Goal can't be reached from the source!")

graph = []
grid = int(input("Enter the size of the grid: "))
print("Enter the adjacency matrix:")
for i in range(grid):
    graph.append(list(map(int, input().split())))
s_x, s_y = map(int, input("Enter source co-ordinates: ").split())
g_x, g_y = map(int, input("Enter goal co-ordinates: ").split())
BFS(graph, s_x, s_y, g_x, g_y)
