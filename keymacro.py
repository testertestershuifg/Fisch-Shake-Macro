import keyboard
import time
import threading

# Define the repeat interval (in seconds)
INTERVAL = 0.2  # Adjust as needed

# Control flag to start/stop the action
running = False

def press_keys():
    global running
    while True:
        if running:
            # Press and release down key
            keyboard.press('s')
            time.sleep(0.05)  # Brief pause to simulate a press
            keyboard.release('s')
            
            # Short delay before pressing enter
            time.sleep(0.05)  
            
            # Press and release enter key
            keyboard.press_and_release('enter')
            
            # Wait before the next iteration
            time.sleep(INTERVAL)
        else:
            time.sleep(0.1)  # Poll every 0.1 second when stopped

def toggle_running(event=None):  # Event argument with default to None
    global running
    running = not running
    if running:
        print("Started")
    else:
        print("Stopped")

# Bind the `]` key to toggle the start/stop of the action
keyboard.add_hotkey(']', toggle_running)


action_thread = threading.Thread(target=press_keys)
action_thread.daemon = True
action_thread.start()

# Keep the program running to listen for the toggle key
keyboard.wait('esc')  # Press ESC to exit the program
