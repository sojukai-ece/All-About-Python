"""
The Challenge: The VIP Bouncer
At the very top of your script, set up your starting data. 
Create a list called guest_ages and fill it with these exact 
numbers: 16, 21, 18, 15, 30, 24, 17, 19.

Next, use the def keyword to build a new machine (function) 
named filter_adults. Inside the parentheses, give this function 
a single parameter named age_list. This is the empty bowl waiting 
to receive the numbers.

Inside the indented block of your function, create a brand new, 
empty list called approved_guests. Next, create a for loop that 
iterates through every single age inside your age_list parameter. 
Inside that loop, use an if statement to check if the age is greater 
than or equal to 18. If it is, use .append() to add that age into 
your approved_guests list. Finally, make sure you step outside of 
the for loop (but stay inside the function) and use the return 
keyword to hand the fully populated approved_guests list back to 
the main program.

Now, step completely outside of your function so you are no longer 
indented. It is time to turn the machine on! Create a new variable 
called vip_list. Set it equal to your filter_adults function, and 
pass your actual guest_ages list into the parentheses as the argument.

Finally, print exactly --- VIP Guest List --- followed by printing 
your new vip_list variable to see the filtered results!
"""

guest_ages = [16, 21, 18, 15, 30, 24, 17, 19]
              
def filter_adults(age_lits):
    approved_guests = []
    for ages in age_lits:
        if ages >= 18:
            approved_guests.append(ages)
    return approved_guests

vip_list = filter_adults(guest_ages)
print(vip_list)
