"""
The Challenge: The Cinema Ticketing System
At the very top of your script, use the def keyword to build 
a small helper machine named calculate_ticket_price. Give it 
a single parameter named age. Inside this function, use if, 
elif, and else statements to check the age and use the return 
keyword to hand back the correct ticket price. If the age is 
less than 12, return 8.00. If the age is greater than or equal 
to 65, return 10.00. For everyone else, return 12.00.

Step outside of that function, and build a second, larger machine 
named process_group_order. Give it a single parameter named 
group_ages (this will expect a list of numbers). Inside this 
function, create a variable called subtotal and set it to 0. Next, 
create a for loop that iterates through every age inside the 
group_ages list.

Here is the magic trick: inside that for loop, you need to add 
money to your subtotal. To get the correct amount, call your 
calculate_ticket_price function, pass in the current age from the 
loop, and add whatever number it returns directly to your subtotal!

Once the for loop finishes running, step outside of the loop (but 
stay inside the process_group_order function). Check if the length 
of the group_ages list is greater than or equal to 5. If it is, 
they get a group discount! Multiply the subtotal by 0.90 (which 
takes 10% off). Finally, use the return keyword to hand the final 
subtotal back to the main program.

Now, step completely outside of both functions so you are no longer 
indented. It is time to turn the main machine on! Create a list called 
family_of_three with the ages [45, 42, 10]. Create a second list called 
party_of_five with the ages [10, 42, 68, 11, 45]. Create a variable 
called family_total and set it equal to your process_group_order function, 
passing in the family list. Create a variable called party_total and set 
it equal to your process_group_order function, passing in the party list.

Finally, print both totals with a nice message, making sure to use your 
:.2f formatting trick so the final costs look like real currency.
"""

def calculate_ticket_price(age):

    if age <= 12:
        return float(8.00)
    elif age >= 65:
        return float(10.00)
    else:
        return float(12.00)
    
def process_group_order(group_ages):
    subtotal = 0
    for age in group_ages:
        subtotal += calculate_ticket_price(age)
    
    if len(group_ages) >= 5:
        subtotal * 0.90
    return subtotal

family_of_three = [45, 42, 10]
party_of_five = [10, 42, 68, 11, 45]

family_total = process_group_order(family_of_three)
party_total = process_group_order(party_of_five)

print(f"The family of three owes: ${family_total:.2f}")
print(f"The party of five owes: ${party_total:.2f}")
