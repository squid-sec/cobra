import pyautogui
import time
import os

def capture_screenshots(output_folder, interval=5, num_screenshots=10):
    """
    Capture screenshots at regular intervals.
    
    Args:
        output_folder (str): Path to the folder where screenshots will be saved.
        interval (int): Time interval between screenshots (in seconds).
        num_screenshots (int): Number of screenshots to capture.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for i in range(num_screenshots):
        screenshot = pyautogui.screenshot()
        filename = os.path.join(output_folder, f"screenshot_{i + 1}.png")
        screenshot.save(filename)
        print(f"Saved screenshot: {filename}")
        time.sleep(interval)

if __name__ == "__main__":
    output_folder = "screenshots"
    interval = 5  # Capture a screenshot every 5 seconds
    num_screenshots = 10  # Total number of screenshots to capture
    
    print("Starting screen capture...")
    capture_screenshots(output_folder, interval, num_screenshots)
    print("Screen capture completed!")
