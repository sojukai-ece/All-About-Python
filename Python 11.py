"""
The Challenge: The Membership Discount Calculator.

At the very top of your script, use the def keyword to create a 
new function named calculate_final_price. Inside the parentheses, 
give this function two parameters: one named price and one named 
is_member.

Inside the indented block of your function, write a simple if 
statement to check if is_member is equal to True. If they are a 
member, calculate a 20% discount (by multiplying the price by 0.80) 
and use the return keyword to send that new discounted price back. 
If they are not a member, use an else statement to simply return 
the original, untouched price.

Once your function is built, go completely outside of it (make sure 
you are no longer indented). Create a variable called alice_total 
and set it equal to your calculate_final_price function, passing in 
15.00 for the price and True for the membership. Below that, create
a variable called bob_total and set it equal to your function again, 
but this time pass in 15.00 for the price and False for the membership.

Finally, print both Alice's total and Bob's total. Make sure to use 
the :.2f formatting trick you learned earlier so the prices look like 
real money!
"""

def calculate_final_price(price, is_member):
    if is_member == True:
        discounted = price * 0.80
        return discounted 
    else:
        return price
    
jiro_total = calculate_final_price(15, True)
jesse_total = calculate_final_price(15, False)

print(jiro_total)
print(jesse_total)
