"""
You have an ESP32 reading data from an older 10-bit Analog-to-Digital Converter (ADC). 
Because the wiring is a bit loose, the serial data coming in is messy.

Sometimes it sends a clean integer. Sometimes it sends the number as a text string. 
Sometimes it completely glitches out and just sends the word "ERROR".

Your Mission: Write a script to process this incoming data stream. 
You need to clean it up, translate the strings into integers, and flag any dangerous readings.


The Requirements
1. Loop through the stream: Process each item in the incoming_data list.

2. Catch the glitches: If the reading is exactly the text "ERROR", print a warning message and ignore that reading.

2. Fix the trap: If it is a valid reading (whether it came in as text or a number), make sure it is converted into a pure integer so you can do math with it.

3. Check for maximums: A 10-bit ADC maxes out at 1023. If the integer value is exactly 1023, print an alert saying "Warning: Sensor Peaked!".

4. Log the rest: If the reading is valid and under the maximum, use an f-string to print a clean log like: "Data logged successfully: 512".
"""

# The messy data arriving from the serial monitor
incoming_data = [512, "490", "ERROR", "1023", 15, "ERROR", 800]

# --- YOUR LOGIC GOES HERE ---
# 1. Start your for loop
    
    # 2. Check if the reading is an "ERROR" first
    
    # 3. If it's not an error, safely translate it to an integer using int()
    
    # 4. Check if the translated integer has hit the 1023 peak
    
    # 5. Otherwise, use an f-string to print the normal reading

for data in incoming_data:
    if data == "ERROR":
        print("Warning, error detected!")
    else:
        clean_reading = int(data)
    if data == "1023":
        print("Note: Data peak detected")
    else:
        print("Data complete!")




