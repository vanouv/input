import math
import time
import pyautogui
import keyboard
import tkinter as tk
from threading import Thread

class MouseJigglerApp:
    def __init__(self, master):
        self.master = master
        master.title("Prevent Screen Lock")
        master.geometry("300x100")
        master.configure(bg="white")  # Set background color to white
        master.resizable(False, False)  # Make the GUI non-resizable

        self.label = tk.Label(master, text="If this script runs press SPACEBAR to stop this script", bg="white")
        self.label.pack(pady=20)

        self.start_button = tk.Button(master, text="Start", command=self.start_jiggler)
        self.start_button.pack()

    def start_jiggler(self):
        self.label.config(text="Press SPACEBAR to stop.", bg="white")
        self.start_button.config(state=tk.DISABLED)

        # Run the mouse jiggler in a separate thread
        thread = Thread(target=self.jiggle_mouse, args=(100, 0.01))
        thread.start()

    def jiggle_mouse(self, radius, speed):
        screen_width, screen_height = pyautogui.size()
        center_x, center_y = screen_width // 2, screen_height // 2

        angle = 0

        try:
            while True:
                # Check if the spacebar is pressed
                if keyboard.is_pressed('space'):
                    break

                # Calculate the coordinates of the point on the circle
                x = center_x + int(radius * math.cos(angle))
                y = center_y + int(radius * math.sin(angle))

                # Move the mouse to the calculated coordinates
                pyautogui.moveTo(x, y, duration=speed)

                # Update the angle for the next iteration
                angle += 0.01

                # Simulate a keypress (e.g., 'a') to prevent system standby
                keyboard.press_and_release('a')

                # Sleep for a short duration to control the speed
                time.sleep(0.01)

        except KeyboardInterrupt:
            pass
        finally:
            # Enable the start button after stopping the script
            self.master.after(0, self.start_button.config, {'state': tk.NORMAL})


if __name__ == "__main__":
    root = tk.Tk()
    app = MouseJigglerApp(root)
    root.mainloop()