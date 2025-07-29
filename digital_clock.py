
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




<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Digital Clock</title>
  <style>
    body {
      background-color: black;
      color: cyan;
      font-family: Arial, sans-serif;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      margin: 0;
    }

    #clock {
      font-size: 60px;
      font-weight: bold;
      background-color: black;
      padding: 20px 40px;
      border: 2px solid cyan;
      border-radius: 10px;
    }
  </style>
</head>
<body>
  <div id="clock">00:00:00 AM</div>

  <script>
    function updateClock() {
      const now = new Date();
      let hours = now.getHours();
      let minutes = now.getMinutes();
      let seconds = now.getSeconds();
      let ampm = hours >= 12 ? 'PM' : 'AM';

      hours = hours % 12 || 12;
      hours = String(hours).padStart(2, '0');
      minutes = String(minutes).padStart(2, '0');
      seconds = String(seconds).padStart(2, '0');

      document.getElementById("clock").textContent = `${hours}:${minutes}:${seconds} ${ampm}`;
    }

    setInterval(updateClock, 1000);
    updateClock(); // call immediately on load
  </script>
</body>
</html>
