# WhatsApp Message Scheduler with Auto-Send

A simple Python application to schedule and send WhatsApp messages automatically using WhatsApp Web. Built with `pywhatkit`, `pyautogui`, and `tkinter`, this tool provides a user-friendly interface to automate your messaging.

---

## Features

- Schedule WhatsApp messages
- Automatically types and sends the message
- Easy-to-use GUI
- Input validation and error handling
- Message logging with timestamps

---

## Requirements

Install the required Python libraries:

```bash
pip install pywhatkit pyautogui


How to Run:
-> Clone the repository:
git clone https://github.com/vinitv5singh/whatsapp-scheduler.git
cd whatsapp-scheduler

-> Run the script:
python automate.py

-> Fill in the details:
Phone Number (with country code, e.g., +91...)
Message
Hour and Minute (in 24-hour format)
Click Schedule Message
The browser will open WhatsApp Web, and the message will be typed and sent automatically.

How It Works:
-> pywhatkit opens WhatsApp Web and types the message.

-> pyautogui presses Enter after a short delay to send it.

-> Each message is logged in message_log.txt with a timestamp.

