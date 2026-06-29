"""
You are monitoring a smart greenhouse.
The ESP32 reads humidity values and decides whether to trigger the misting system, do nothing,
or trigger the dehumidifier.

The Instructions

Iterate: Loop through the humidity_data list.
Filter: If the reading is "SENSOR_FAIL", print "Error: Sensor failure. Checking next log...".

Evaluate (3 States):
If humidity is below 30%, print: "Misting system ON (Dry: {value}%)"
If humidity is above 70%, print: "Dehumidifier ON (Humid: {value}%)"
Otherwise (between 30% and 70%), print: "Status: Optimal ({value}%)"

Count: Keep a running count of how many times the status was "Optimal".

Summary: Print the final count of optimal readings using an f-string.
"""

humidity_data = [25, 45, "SENSOR_FAIL", 80, 55, "SENSOR_FAIL", 30]

optimal_count = 0

for humid in humidity_data:
    if humid == "SENSOR_FAIL":
        print(f"Error: Sensor failure. Checking next log...")
    else:
        value = int(humid)
        if humid > 30:
            print(f"Misting system ON (Dry: {value}%)")
        elif humid > 70:
            print(f"Dehumidifier ON (Humid: {value}%)")
        else:
            print(f"Status: Optimal ({value}%)")
            optimal_count = optimal_count + 1

print(f"Total optimal readings: {optimal_count}")
       
 
