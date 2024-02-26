def Input():
     global container 
     container = list(map(int,input("Enter list elements : ").split()))
      
def OddListCount():
    odd_count = 0
    for i in container: 
          if(i%2==0): odd_count+=1 
    print("The number odd numbers in the list is", odd_count)
    
def EvenListCount():
    even_count = 0
    for i in container: 
          if(i%2==0): even_count+=1 
    print("The number even numbers in the list is", even_count)
      
Input()
OddListCount()
EvenListCount()
