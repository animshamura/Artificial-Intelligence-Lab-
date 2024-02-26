def Input():
     global container 
     container = tuple(input("Enter tuple elements : ").split())
      
def Print():
      print(f"The 4th element from the beginning : {container[3]}")
      print(f"The 4th element from the last : {container[len(container)-4]}")
      
Input()
Print()
