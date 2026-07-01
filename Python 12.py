"""
The Challenge: The Road Trip Estimator
At the very top of your script, use the def keyword to build a 
new machine (function) named estimate_trip_cost. Inside the parentheses, 
give this function three parameters: distance, mpg (which stands for 
miles per gallon), and gas_price.

Inside the indented block of your function, you need to do two quick 
math equations. First, calculate how many gallons of gas the trip will 
require by dividing the distance by the mpg. Save this into a new variable 
called gallons_needed. Next, calculate the total_cost by multiplying those 
gallons_needed by the gas_price. Finally, use the return keyword to hand 
that total_cost back to the main program.

Now, step completely outside of your function so you are no longer indented. 
It is time to turn the machine on and feed it some real data!

Create a variable called weekend_getaway and set it equal to your estimate_trip_cost function.
Pass in 400 for the distance, 25 for the mpg, and 3.50 for the gas price. 
Right below that, create another variable called daily_commute and set it equal 
to your function again, but this time pass in 30 for the distance, 25 for the mpg, 
and 3.50 for the gas price.

Finally, print both of those variables to the screen with a nice message. Make sure 
to use the :.2f formatting trick so the final costs look like standard currency!
"""
def estimate_trip_cost(distance, mpg, gas_price):
    gallons_needed = distance / mpg
    total_cost = gallons_needed / gas_price
    return total_cost

weekend_giatay = estimate_trip_cost(400, 25, 3.50)
daily_hindi_cute = estimate_trip_cost(30, 25, 3.50)

print(f"Getaway cost: ${weekend_giatay:.2f}")
print(f"Commute cost: ${daily_hindi_cute:.2f}")
