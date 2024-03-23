# Author - Shamura Ahmad 
step =  ["down","up","right","left"]

def DFS(graph,s_x,s_y,g_x,g_y,depth):
     global found
     found = False
     graph[s_x][s_y] = 0
     for i in range(4):
         n_x = s_x + (((-1)**(i%2)) if i < 2 else 0)
         n_y = s_y + (((-1)**(i%2)) if i > 1 else 0)
         if( (n_x and n_y) in range(len(graph)) and graph[n_x][n_y]==1):
                 depth +=1
                 print(f"Moving {step[i]} to ({n_x},{n_y})")
                 if(n_x == g_x and n_y == g_y):
                     print("Goal found!")
                     print(f"Number of moves required : {depth} ")
                     found = True
                     return
                 else: DFS(graph,n_x,n_y,g_x,g_y,depth)
         if found: return 
     
graph = []
grid = int(input("Enter the size of the grid : "))
print("Enter the adjacency matrix : ")
for i in range(grid): graph.append(list(map(int, input().split())))
s_x, s_y = map(int, input("Enter source co-ordinates : ").split())
g_x, g_y = map(int, input("Enter goal co-ordinates : ").split())
DFS(graph, s_x, s_y, g_x, g_y,0)
if not found: print("Goal can't be reached from the source!")

    

    