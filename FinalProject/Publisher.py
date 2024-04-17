import paho.mqtt.client as mqtt
import json
import time
import tkinter as tk
from tkinter import messagebox
import group_5_util

PORT = 1883

class PublisherGUI:
    def __init__(self, master):
        self.master = master
        master.title("Publisher")

        # Connect and Disconnect Buttons
        self.connect_button = tk.Button(master, text="Connect")
        self.connect_button.grid(row=0, column=0, padx=5, pady=5)

        self.disconnect_button = tk.Button(master, text="Disconnect")
        self.disconnect_button.grid(row=0, column=1, padx=5, pady=5)

        # Min Value, Max Value, Daily Mean, Readings Per Day Labels and Textboxes
        self.min_label = tk.Label(master, text="Min Value:")
        self.min_label.grid(row=1, column=0, sticky="e", padx=5)
        self.min_entry = tk.Entry(master)
        self.min_entry.grid(row=1, column=1, padx=5)

        self.max_label = tk.Label(master, text="Max Value:")
        self.max_label.grid(row=2, column=0, sticky="e", padx=5)
        self.max_entry = tk.Entry(master)
        self.max_entry.grid(row=2, column=1, padx=5)

        self.mean_label = tk.Label(master, text="Daily Mean:")
        self.mean_label.grid(row=3, column=0, sticky="e", padx=5)
        self.mean_entry = tk.Entry(master)
        self.mean_entry.grid(row=3, column=1, padx=5)

        self.readings_label = tk.Label(master, text="Readings Per Day:")
        self.readings_label.grid(row=4, column=0, sticky="e", padx=5)
        self.readings_entry = tk.Entry(master)
        self.readings_entry.grid(row=4, column=1, padx=5)

        # Update Button
        self.update_button = tk.Button(master, text="Update")
        self.update_button.grid(row=5, columnspan=2, pady=5)

        # Start Publishing and Stop Publishing Buttons
        self.start_publishing_button = tk.Button(master, text="Start Publishing")
        self.start_publishing_button.grid(row=6, column=0, padx=5, pady=5)

        self.stop_publishing_button = tk.Button(master, text="Stop Publishing")
        self.stop_publishing_button.grid(row=6, column=1, padx=5, pady=5)

        # Topic Label and Textbox
        self.topic_label = tk.Label(master, text="Topic:")
        self.topic_label.grid(row=7, column=0, padx=5, pady=5)
        self.topic_entry = tk.Entry(master, state="disabled", disabledbackground="lightgray")
        self.topic_entry.grid(row=7, column=1, padx=5, pady=5)
        self.topic_entry.insert(0, "Humidity Over Time")

    def publish_data(self):
        try:
            topic = self.topic_entry.get()
            if not topic:
                raise ValueError("Topic cannot be empty")
            
            client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, 'pub')
            client.connect('localhost', PORT)

            data = group_5_util.create_data()
            string = json.dumps(data)
            client.publish(topic, string)
            print(f"Published: {string}")

            client.disconnect()

            messagebox.showinfo("Success", "Data published successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

def main():
    root = tk.Tk()
    gui = PublisherGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
