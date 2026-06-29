"""
You are processing a batch of data from an IoT aquarium system.
 The system logs the water's pH level and temperature. 
 However, the pH sensor occasionally drops connection and sends the word "OFFLINE" instead of a number. 
 Furthermore, the valid pH readings are arriving as strings, while the temperature arrives as raw numbers.

Your Mission: Clean the data, calculate the average pH level of the tank from the valid readings, and flag any dangerous temperature drops.


PRECISE INSTRUCTIONS:
You must write a top-to-bottom script (no functions) that does exactly the following in order:

Initialize Variables: Before the loop, create two variables: total_ph = 0.0 and valid_readings = 0. You will use these to calculate the average later.

Iterate: Loop through the sensor_logs list.

Check for Offline Data: For each reading, check if the "pH" value is exactly the string "OFFLINE".

If it is offline: Print "Warning: pH sensor offline. Skipping reading." and do nothing else for that specific reading.

Process Valid Data: If the reading is not offline:

Translate the "pH" string into a decimal number using float() and assign it to a new variable.

Add that new decimal number to your total_ph variable.

Add 1 to your valid_readings variable.

Check the Vitals: Still inside the valid data block, check the "temp" value.

If the temperature drops below 20.0, print a warning using an f-string: "SOS: Water temperature too low! (Current: {temp_variable}C)".

Calculate the Average: Completely outside and after the loop, calculate the final average pH by dividing total_ph by valid_readings.

Final Output: Print the final average using an f-string: "System Check Complete. Average pH: {average_variable}".

"""


# The batch data from the IoT aquarium system
sensor_logs = [
    {"pH": "7.1", "temp": 24.5},
    {"pH": "OFFLINE", "temp": 24.0},
    {"pH": "7.3", "temp": 24.2},
    {"pH": "6.8", "temp": 19.5},  # This should trigger the low temp warning!
    {"pH": "OFFLINE", "temp": 24.1},
    {"pH": "7.2", "temp": 23.8}
]

# 1. Initialize your variables here
total_ph = 0.0
valid_readings = 0

# 2. Start your loop here
for log in sensor_logs:
    
    # Extract the values to make your life easier
    current_ph = log["pH"]
    current_temp = log["temp"]
    
    # --- YOUR LOGIC GOES HERE ---
    # 3. Check for "OFFLINE"
    
    # 4 & 5. Process valid data (float translation, addition, and temp check)
    

# --- FINAL MATH AND OUTPUT GOES HERE ---
# 6. Calculate average

# 7. Print final summary
