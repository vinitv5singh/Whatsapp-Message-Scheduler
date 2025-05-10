import pywhatkit
import pyautogui
import tkinter as tk
from tkinter import messagebox
import datetime
import time

def send_message():
    phone = phone_entry.get().strip()
    message = msg_entry.get("1.0", tk.END).strip()
    hour = hour_entry.get().strip()
    minute = minute_entry.get().strip()

    try:
        # Validate input
        hour = int(hour)
        minute = int(minute)
        if not (0 <= hour <= 23 and 0 <= minute <= 59):
            raise ValueError("Invalid time")

        if not phone.startswith("+") or len(phone) < 10:
            raise ValueError("Invalid phone number format")

        if not message:
            raise ValueError("Message is empty")

        # Schedule message
        pywhatkit.sendwhatmsg(phone, message, hour, minute, wait_time=10)

        # Wait until message is typed (pywhatkit handles some of this, then we wait)
        time.sleep(15)

        # Press Enter to send
        pyautogui.press("enter")

        # Log message
        with open("message_log.txt", "a") as log:
            log.write(f"{datetime.datetime.now()} | To: {phone} | At: {hour}:{minute} | Message: {message}\n")

        messagebox.showinfo("Success", "Message scheduled and sent successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"Failed to send message:\n{str(e)}")

# GUI setup
app = tk.Tk()
app.title("WhatsApp Message Scheduler")
app.geometry("400x400")

tk.Label(app, text="Phone Number (+countrycode)").pack()
phone_entry = tk.Entry(app, width=30)
phone_entry.pack()

tk.Label(app, text="Message").pack()
msg_entry = tk.Text(app, height=5, width=30)
msg_entry.pack()

tk.Label(app, text="Hour (24-hr format)").pack()
hour_entry = tk.Entry(app, width=10)
hour_entry.pack()

tk.Label(app, text="Minute").pack()
minute_entry = tk.Entry(app, width=10)
minute_entry.pack()

tk.Button(app, text="Schedule Message", command=send_message).pack(pady=10)

app.mainloop()
