import pywhatkit
import tkinter as tk
from tkinter import simpledialog, messagebox
from datetime import datetime, timedelta
import pyautogui

class WhatsAppMessageSender:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("WhatsApp Message Sender :D")
        self.group_id = None
        self.message_text = None
        self.send_option = None
        self.send_time = None

        # Increase the window dimensions
        self.root.geometry("600x250")

        # Create the main frame
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack()

        # Create a label for clear space above the title in "Send to Group" tab
        clear_label_group = tk.Label(self.main_frame, text="", height=1)
        clear_label_group.pack()

        # Create title label for "Send to Group" tab
        self.group_title_label = tk.Label(self.main_frame, text="Send a Message to a Group", font=("Helvetica", 20, "bold"))
        self.group_title_label.pack()
        
        # Create buttons for options
        self.group_button = tk.Button(self.main_frame, text="Send to Group", command=self.send_to_group, width=20, height=2)
        self.group_button.pack(pady=10)

        # Create a label for clear space above the title in "Send to Person" tab
        clear_label_person = tk.Label(self.main_frame, text="", height=1)
        clear_label_person.pack()

        # Create title label for "Send to Person" tab
        self.person_title_label = tk.Label(self.main_frame, text="Send a Message to a Person", font=("Helvetica", 20, "bold"))
        self.person_title_label.pack()

        self.person_button = tk.Button(self.main_frame, text="Send to Person", command=self.send_to_person, width=20, height=2)
        self.person_button.pack(pady=10)

        # Run the Tkinter event loop
        self.root.mainloop()

    def send_to_group(self):
        # Prompt user for group ID
        self.group_id = simpledialog.askstring("Input", "Enter Group ID:")
        if not self.group_id:
            return

        # Prompt user for message
        self.message_text = simpledialog.askstring("Input", "Enter Message:")
        if not self.message_text:
            return

        # Prompt user for send time
        self.send_time = simpledialog.askstring("Input", "Enter Time (HH:MM):")
        if not self.send_time:
            return

        self.send_once()

    def send_to_person(self):
        # Prompt user for contact number
        contact_number = simpledialog.askstring("Input", "Enter Contact Number:")
        if not contact_number:
            return

        # Prompt user for message
        self.message_text = simpledialog.askstring("Input", "Enter Message:")
        if not self.message_text:
            return

        # Prompt user for send time
        self.send_time = simpledialog.askstring("Input", "Enter Time (HH:MM):")
        if not self.send_time:
            return

        self.send_once_to_person(contact_number)

    def send_once(self):
        try:
            # Split the time input into hours and minutes
            hours, minutes = map(int, self.send_time.split(':'))

            # Calculate time difference between now and the specified time
            now = datetime.now()
            send_datetime = datetime(now.year, now.month, now.day, hours, minutes)

            # Check if the specified time is in the future
            if send_datetime <= now:
                send_datetime += timedelta(days=1)  # Add a day if the time is in the past

            # Calculate the delay in seconds
            delay_seconds = (send_datetime - now).total_seconds()

            # Send the WhatsApp message for the specified time
            pywhatkit.sendwhatmsg_to_group(self.group_id, self.message_text, hours, minutes, wait_time=delay_seconds, tab_close=True)

            # Simulate pressing Enter and clicking after typing the message
            self.root.after(int(delay_seconds * 1000) + 2000, lambda: pyautogui.press('enter'))
            self.root.after(int(delay_seconds * 1000) + 4000, lambda: pyautogui.click())

            # Add an additional delay before sending the message
            self.root.after(int(delay_seconds * 1000) + 6000, self.send_message_delay)

            messagebox.showinfo("done", f"message timed to be sent at {send_datetime}")

        except ValueError:
            messagebox.showinfo("problem", "problem with the time. Please enter time with the HH:MM format.")

    def send_once_to_person(self, contact_number):
        try:
            # Split the time input into hours and minutes
            hours, minutes = map(int, self.send_time.split(':'))

            # Calculate time difference between now and the specified time
            now = datetime.now()
            send_datetime = datetime(now.year, now.month, now.day, hours, minutes)

            # Check if the specified time is in the future
            if send_datetime <= now:
                send_datetime += timedelta(days=1)  # Add a day if the time is in the past

            # Calculate the delay in seconds
            delay_seconds = (send_datetime - now).total_seconds()

            # Send the WhatsApp message to the specified contact for the specified time
            pywhatkit.sendwhatmsg(contact_number, self.message_text, hours, minutes, wait_time=delay_seconds, tab_close=True)

            # Simulate pressing Enter and clicking after typing the message
            self.root.after(int(delay_seconds * 1000) + 2000, lambda: pyautogui.press('enter'))
            self.root.after(int(delay_seconds * 1000) + 4000, lambda: pyautogui.click())

            # Add an additional delay before sending the message
            self.root.after(int(delay_seconds * 1000) + 6000, self.send_message_delay)

            messagebox.showinfo("done", f"message timed to be sent to {contact_number} at {send_datetime} :D")

        except ValueError:
            messagebox.showinfo("problem", "problem with the time. Please enter time with the HH:MM format.")

    def send_message_delay(self):
        # Simulate pressing Enter and clicking to send the message
        pyautogui.press('enter')
        pyautogui.click()

# Instantiate the WhatsAppMessageSender class
app = WhatsAppMessageSender()
