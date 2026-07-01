"""
The Challenge: The RPG Loot Manager
At the very top of your script, set up your starting data. 
First, create a dictionary called player_inventory and fill 
it with these exact key-value pairs: "health potion": 2 and 
"gold coin": 15. Right below that, create a list called 
dropped_loot and fill it with these exact strings: "gold coin", 
"magic sword", "health potion", and "gold coin". Notice that 
"gold coin" appears twice in the list!

Next, use the def keyword to build a new machine named gather_loot. 
Inside the parentheses, give this function two parameters: 
current_inventory (which will expect a dictionary) and new_items 
(which will expect a list).

Inside the indented block of your function, create a for loop 
that iterates through every single item inside your new_items 
parameter. Inside that loop, use an if statement to check if the 
item already exists inside your current_inventory dictionary. If 
it does exist, add 1 to its current value. If it does not exist, 
use an else statement to add it to the dictionary and set its 
starting value to 1. Once the loop is completely finished sorting 
the items, step outside of the for loop and use the return keyword 
to hand the updated current_inventory back to the program.

Now, step completely outside of your function so you are no longer 
indented. It is time to turn the machine on! Create a variable called 
final_inventory and set it equal to your gather_loot function, passing 
in your actual player_inventory dictionary and your dropped_loot list 
as the arguments.

Finally, print exactly --- Final Inventory ---. Then, write a quick 
for loop to iterate through the .items() of your new final_inventory 
variable, printing each item name and its total quantity to the screen.
"""

player_inventory = {"health potion": 2,
    "gold coin": 15}
    
dropped_loot = ["gold coin", "health potion", "magic sword", "gold coin"]

def gather_loot(current_inventory, new_items):

    for item in new_items:
        if item in current_inventory:
            current_inventory[item] += 1 
        else:
            current_inventory[item] = 1
    return current_inventory

final_inventory = gather_loot(player_inventory, dropped_loot)

for item, amount in final_inventory.items():
    print(f"{item}: {amount}")
