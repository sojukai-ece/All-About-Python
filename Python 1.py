"""
Imagine you are testing the logic for a wearable safety device. 
The microcontroller processes data in batches and sends a list of recent readings. 
Each reading contains a simulated heart rate (in beats per minute) and the status of a physical panic button on the device.

Your Mission: Write a script that checks each reading in the batch.
If it detects a critical situation, 
it should print an alert and keep a running count of how many times an SOS was triggered.
"""

sensor_batch = [
    {"heart_rate": 75, "panic_button": False},
    {"heart_rate": 48, "panic_button": False},  # Low heart rate!
    {"heart_rate": 82, "panic_button": False},
    {"heart_rate": 90, "panic_button": True},   # Button pressed!
    {"heart_rate": 165, "panic_button": False}, # High heart rate!
    {"heart_rate": 80, "panic_button": False}
]
for reading in sensor_batch:
    
    # 2. Extract the actual values into variables
    current_hr = reading["heart_rate"]
    button_pressed = reading["panic_button"]

    if current_hr >= 90:
        print("Emergency pulse rate detected!")
    elif button_pressed == True:
        print("Panic Button is Pushed!")
    else: 
        print("Everything is stable!")



