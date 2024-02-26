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

        self.root.geometry("600x250")

        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack()

        clear_label_group = tk.Label(self.main_frame, text="", height=1)
        clear_label_group.pack()

        self.group_title_label = tk.Label(self.main_frame, text="Send a Message to a Group", font=("Helvetica", 20, "bold"))
        self.group_title_label.pack()

        self.group_button = tk.Button(self.main_frame, text="Send to Group", command=self.send_to_group, width=20, height=2)
        self.group_button.pack(pady=10)

        clear_label_person = tk.Label(self.main_frame, text="", height=1)
        clear_label_person.pack()

        self.person_title_label = tk.Label(self.main_frame, text="Send a Message to a Person", font=("Helvetica", 20, "bold"))
        self.person_title_label.pack()

        self.person_button = tk.Button(self.main_frame, text="Send to Person", command=self.send_to_person, width=20, height=2)
        self.person_button.pack(pady=10)

        self.root.mainloop()

    def send_to_group(self):
        self.group_id = simpledialog.askstring("Input", "Enter Group ID:")
        if not self.group_id:
            return

        self.message_text = self.create_multiline_input("Enter Message:")

        self.send_time = simpledialog.askstring("Input", "Enter Time (HH:MM):")
        if not self.send_time:
            return

        self.send_once()

    def send_to_person(self):
        contact_number = simpledialog.askstring("Input", "Enter Contact Number:")
        if not contact_number:
            return

        self.message_text = self.create_multiline_input("Enter Message:")

        self.send_time = simpledialog.askstring("Input", "Enter Time (HH:MM):")
        if not self.send_time:
            return

        self.send_once_to_person(contact_number)

    def create_multiline_input(self, prompt):
        input_window = tk.Toplevel(self.root)
        input_window.title(prompt)
        
        input_text = tk.Text(input_window, wrap='word', width=40, height=5)
        input_text.pack(pady=10)
        
        ok_button = tk.Button(input_window, text="OK", command=lambda: self.set_input_text(input_text, input_window))
        ok_button.pack(pady=5)

        self.root.wait_window(input_window)

        return self.input_text

    def set_input_text(self, input_text_widget, input_window):
        self.input_text = input_text_widget.get("1.0", "end-1c")
        input_window.destroy()

    def send_once(self):
        try:
            hours, minutes = map(int, self.send_time.split(':'))
            now = datetime.now()
            send_datetime = datetime(now.year, now.month, now.day, hours, minutes)

            if send_datetime <= now:
                send_datetime += timedelta(days=1)

            delay_seconds = (send_datetime - now).total_seconds()

            pywhatkit.sendwhatmsg_to_group(self.group_id, self.message_text, hours, minutes, wait_time=delay_seconds, tab_close=True)

            self.root.after(int(delay_seconds * 1000) + 2000, lambda: pyautogui.press('enter'))
            self.root.after(int(delay_seconds * 1000) + 4000, lambda: pyautogui.click())

            self.root.after(int(delay_seconds * 1000) + 6000, self.next_functionality)

            messagebox.showinfo("done", f"message timed to be sent at {send_datetime}")

        except ValueError:
            messagebox.showinfo("problem", "problem with the time. Please enter time with the HH:MM format.")

    def send_once_to_person(self, contact_number):
        try:
            hours, minutes = map(int, self.send_time.split(':'))
            now = datetime.now()
            send_datetime = datetime(now.year, now.month, now.day, hours, minutes)

            if send_datetime <= now:
                send_datetime += timedelta(days=1)

            delay_seconds = (send_datetime - now).total_seconds()

            pywhatkit.sendwhatmsg(contact_number, self.message_text, hours, minutes, wait_time=delay_seconds, tab_close=True)

            self.root.after(int(delay_seconds * 1000) + 2000, lambda: pyautogui.press('enter'))
            self.root.after(int(delay_seconds * 1000) + 4000, lambda: pyautogui.click())

            self.root.after(int(delay_seconds * 1000) + 6000, self.next_functionality)

            messagebox.showinfo("done", f"message timed to be sent to {contact_number} at {send_datetime} :D")

        except ValueError:
            messagebox.showinfo("problem", "the is a no no problem with the time. Please enter time with the HH:MM format.")

    def next_functionality(self):
        pass

app = WhatsAppMessageSender()
