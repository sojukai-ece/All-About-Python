"""
Step-by-Step Requirements
Display the Menu: Iterate through the menu dictionary and print each item and its price, 
formatted to two decimal places (e.g., Espresso: $2.50).

Accept Orders: Use a while loop to continuously prompt the user for an item.
The input prompt should say: Enter an item to order (or 'done' to finish): 

Handle Input Logic:
Standardize Input: Ensure the user's input is converted to lowercase and stripped of any leading/trailing 
whitespace so it matches the dictionary keys.

Exit Condition: If the user types done, immediately break out of the loop.

Valid Order: If the item exists in the menu, add its price to a running subtotal 
and print a confirmation message (e.g., Added latte.).

Invalid Order: If the item does not exist in the menu, print exactly: 
Sorry, that item is not on the menu. Do not add anything to the subtotal.

Calculate Discount: After the loop ends, check if the running subtotal is strictly greater than $15.00.

If it is, calculate a 10% discount on the subtotal.

If it is not, the discount is 0.

Calculate Tax: Apply a 5% tax to the discounted subtotal.

Print the Receipt: Print a final summary displaying the original subtotal, 
the discount amount, the tax amount, and the final total. All financial values must be rounded and formatted to exactly two decimal places.

"""

menu = {
    "espresso": 2.50,
    "latte": 3.75,
    "muffin": 2.00,
    "cake": 4.50,
    "tea": 2.25
}

for display, price in menu.items():
    print(f"{display.capitalize()}: ${price:.2f}")

subtotal = 0.0

while True:
   order = input("Plese enter your order: ").strip().lower()

   if order == 'done':
       break
   if order in menu:
       subtotal += menu[order]
       print(f"Added {order}")
   else:
       print("Sorry we couldn't find your order")

discount = 0.0

if subtotal > 15.00:
    discount = subtotal * 0.10

discounted_subtotal = subtotal - discount

tax = discounted_subtotal * 0.5

final_total = discounted_subtotal + tax

print("---Final Receipt---")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Discount (10%): -${discount:.2f}")
print(f"Tax (5%): ${tax:.2f}")
print(f"Final Total: ${final_total:.2f}")



    
    
