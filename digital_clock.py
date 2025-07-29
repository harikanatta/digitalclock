
from tkinter import *
import time

def update_time():
    current_time = time.strftime("%H:%M:%S %p")  # Format: Hours:Minutes:Seconds AM/PM
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)  # Update every 1 second

# GUI window setup
root = Tk()
root.title("Digital Clock")
root.geometry("400x200")
root.resizable(False, False)
root.configure(bg="black")

# Label to display time
clock_label = Label(root, font=("Arial", 50, "bold"), bg="black", fg="cyan")
clock_label.pack(pady=40)

# Start the clock
update_time()

# Start the GUI event loop
root.mainloop()





 
