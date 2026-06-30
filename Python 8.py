"""
The Challenge: The Dynamic To-Do List
Objective: Write a script that acts as an interactive task manager, 
allowing a user to continuously add tasks, check them off, or quit the program.

Step-by-Step Requirements
Setup: Create an empty list named tasks at the very top of your script.

Main Loop: Start a while True: loop.

Display Status: At the start of the loop, check the length of the tasks list.

If it is empty, print exactly: \n--- To-Do List --- \nYour list is empty.
If it has items, print \n--- To-Do List --- followed by every task in the list (use a for loop to print them one by one).
Menu Prompt: Ask the user: Choose an action (add, done, quit):  and convert their input to lowercase.
Quit Logic: If the user types quit, break the loop.
Add Logic: If the user types add, prompt them with Enter task to add: .
Add their input to the tasks list using .append().
Done Logic: If the user types done, prompt them with Enter task to complete: .
Check if their exact input exists inside the tasks list.
If it does, remove it using .remove().
If it does not, print exactly: Task not found.
Invalid Command: If the user types anything other than add, done, or quit, print exactly: Invalid command.
"""

# 1. Setup
tasks = []

# 2. Main Loop
while True:
    # 3. Display Status
    print("\n--- To-Do List ---")
    if len(tasks) == 0:
        print("Your list is empty.")
    else:
        for task in tasks:
            print(task)
            
    # 4. Menu Prompt
    action = input("Choose an action (add, done, quit): ").lower().strip()
    
    # 5. Quit Logic
    if action == "quit":
        break
        
    # 6. Add Logic
    elif action == "add":
        new_task = input("Enter task to add: ")
        tasks.append(new_task)
        
    # 7. Done Logic
    elif action == "done":
        completed_task = input("Enter task to complete: ")
        if completed_task in tasks:
            tasks.remove(completed_task)
        else:
            print("Task not found.")
            
    # 8. Invalid Command
    else:
        print("Invalid command.")
        

