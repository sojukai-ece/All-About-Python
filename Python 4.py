"""
The Scenario: ESP8266 Mini Robot Navigation
The ultrasonic sensor on your ESP8266 mini robot sends a batch of distance readings (in centimeters).
Some readings arrive as raw numbers, some as text strings, and missed pings return the exact word "TIMEOUT".

The Instructions
Write a top-to-bottom script to process this batch:

Initialize: Create a variable collision_count = 0 before the loop.
Iterate: Loop through the sensor_pings list.
Filter: If the reading is "TIMEOUT", print "Ping lost. Skipping..." and do nothing else for that reading.
Translate: For all valid readings, translate the data into an integer.
Evaluate: * If the distance is less than 14 cm, print an f-string: "COLLISION ALERT! Object at {distance} cm." 
and add 1 to collision_count.

Otherwise, print an f-string: "Path clear: {distance} cm."
Summary: Outside the loop at the very end, print an f-string: "Total collision warnings: {collision_count}".

"""

# Batch data from the robot's ultrasonic sensor
sensor_pings = [120, "85", "TIMEOUT", "12", 45, "TIMEOUT", "8"]

# 1. Initialize your variable here
collision_count = 0 

# 2. Start your loop here
for data in sensor_pings:
    # 3. Check for "TIMEOUT"
    if data == "TIMEOUT":
        print("Ping lost. Skipping...")
    else:
        # 4 & 5. Translate to integer and check distance
        print("Everything is stable... Proceeding...")
        distance = int(data)
        if distance > 14:
            print(f"COLLISION ALERT! Object at {distance} cm.")
            collision_count = collision_count + 1
        else:
            print("Everything is clear...")
    
# FINAL OUTPUT 
# 6. Print the summary
print(f"Total collision warnings: {collision_count}")
