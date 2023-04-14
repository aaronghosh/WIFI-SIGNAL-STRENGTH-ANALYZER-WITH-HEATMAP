import subprocess
import re
import time
import csv


# Function to get the signal strength of the connected WiFi network
# Function to get the signal strength of the connected WiFi network in dBm
def get_signal_strength():
    # Run the command to get the signal strength and capture the output
    cmd_output = subprocess.check_output(["netsh", "wlan", "show", "interfaces"])
    cmd_output = cmd_output.decode("ascii")
    print(cmd_output)

    # Search for the signal strength in the output using regular expressions
    signal_strength_search = re.search("Signal\s*: (\d+)%", cmd_output)

    # If the signal strength is found, calculate it in dBm and return it as an integer, otherwise return None
    if signal_strength_search:
        signal_strength = int(signal_strength_search.group(1))
        signal_strength_dbm = int((signal_strength / 2) - 100)
        return signal_strength_dbm
    else:
        return None

# Define the filename to save the signal strength data to
filename = 'signal_strength.csv'

# Open the CSV file and write the header row
with open(filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Timestamp', 'Signal Strength'])

# Define the time interval to measure the signal strength (in seconds)
interval = 1

# Start the loop to continuously measure the signal strength
while True:
    # Get the current time and signal strength
    timestamp = time.time()
    signal_strength = get_signal_strength()
    print(f"Signal strength: {signal_strength}")

    # If the signal strength is not None, save it to the CSV file
    if signal_strength is not None:
        with open(filename, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([timestamp, signal_strength])

    # Wait for the next interval
    time.sleep(interval)

    # Stop the loop if a keyboard interrupt is detected
    try:
        pass
    except KeyboardInterrupt:
        break
