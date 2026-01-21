### day 6 challenge ###
### To do app ####

### menu system ; add/create tasks, view tasks, delete tasks, exit

# it is currently day 17 of jan and I am behind on my tasks becasue its been really busy but we are going to get it done #

import os


def load_tasks(): #creating the text file  
    try: 
        with open('todolist.txt', 'w+') as f:
                return f.read().splitlines() # Reads the entire content of the file as a single string and then splits it into a list of lines
    except FileNotFoundError:
        return []
        

def save_tasks(tasks):  # saving the text file
    with open('todolist.txt', 'w') as f:
        for item in tasks:
            f.write(item + "\n")
    
        
          
def main():
    tasks = load_tasks()
    while True:
        print("------------Welcome to DoITby.Joy app----------")
        print("                ")
        print("1. Add tasks")
        print("2. View tasks")
        print("3. Delete tasks")
        print("4. Exit")
        choice = input("Choose your option below: ")
    

        if choice == "1":
            alltasks = input("Add your task here: ")
            tasks.append(alltasks)
            save_tasks(tasks)
    
        elif choice == "2":
            for i, word in enumerate(tasks): #numbers each item in list
                print(f"{i}: {word}")
        
            
        elif choice == "3":
            removeitem =  int(input(" Choose index you want to delete from list: "))
            tasks.pop(removeitem)
            print(tasks)
            save_tasks(tasks)
        
        elif choice == "4":
            exit()  # using exit instead of break solves the else statement still printing problem I was having #
        else: 
            print("Invalid choice try again")   
                          

#file handling 
#fruits = ['apple', 'banana', 'orange' , 'grapes']


                
#f = open('todolist.txt', 'w')

main()