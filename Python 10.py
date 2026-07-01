"""
The Challenge: The University Enrollment System

At the very top of your script, you need to set up your starting data.
Create a dictionary named courses containing "python 101" with 2 seats, 
"data 200" with 1 seat, and "web 350" with 3 seats. Right below that, 
create an empty list named my_schedule that will eventually hold the classes 
the user successfully joins.

Once your data is set up, start an infinite while loop to keep the program running. 
Inside this loop, prompt the user to choose an action by typing either view, enroll,
drop, or quit, and make sure to convert their answer to lowercase so it is easy to check.
If the user types quit, simply break the loop to shut down the program.

If the user types view, you need to show them the catalog. Use a for loop to print 
every course in the dictionary along with its remaining seats. Immediately after that, 
check the length of their my_schedule list. If it is empty, tell them they are not enrolled
in anything. If it has items in it, print out the names of the courses they are currently taking.

If the user decides to type enroll, ask them which specific course they want to join. 
Before you let them in, you must check three conditions using if and elif statements. 
First, check if the course does not exist in the dictionary at all and tell them if so. 
Second, check if the course is already sitting inside their my_schedule list and remind
them they are already taking it. Third, check if the dictionary says that specific 
course has 0 seats left, and apologize that it is full. If the course passes all three of 
those checks, subtract one seat from the dictionary, add the course to their schedule list,
and print a success message.

Finally, if the user types drop, ask them which course they want to remove. 
Check if the course is actually in their schedule list. If it is not, let them know 
they cannot drop a class they are not taking. If it is in their list, remove it, add 
one seat back to the dictionary's availability, and confirm it was dropped. If the user 
types anything other than those four main commands, print a message saying the action is 
invalid so the loop can start over.
"""

#datasets
courses = {
    "python":2,
    "data":1,
    "web":3,
    "ml": 2,
    "embedded":5,
    "vlsi":1
}

my_schedule = []

while True:

    if len(my_schedule) == 0:
        print("Your schedule is empty")
    elif len(my_schedule) == 5:
        print("Reached maximum units")
        break
    else:
        for sched in my_schedule:
            print(sched)

    action = input("Choose an action to take (view, enroll, drop, quit): ").lower().strip()

    if action == "quit":
        break

    elif action == "view":
        print(courses)

    elif action == "enroll":
        new_sched = input(f"Which course you want to enroll in? {courses}: ")
        if new_sched not in courses:
            print("Error, course not found")
        elif new_sched in my_schedule:
            print("You are already enrolled in this course.")
        elif courses[new_sched] == 0:
            print(f"This course is already full")
        else:
            courses[new_sched] -= 1
            my_schedule.append(new_sched)
            print(f"Successfully enrolled in {new_sched}")

    elif action == "drop":
        drop_course = input(f"Enter course to drop: ")
        if drop_course in my_schedule:
            my_schedule.remove(drop_course)
        else:
            print("Course not found")
    
    else:
        print("Invalid action, please try again")
