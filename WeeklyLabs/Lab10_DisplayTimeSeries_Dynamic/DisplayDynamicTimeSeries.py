from tkinter import *
from tkinter import messagebox
import random
import threading
import time

class DisplayDynamicDataSeries:
    def __init__(self, base_min=18, base_max=21):
        self.base_min = base_min
        self.base_max = base_max
        self.values = [self._generate_random_temperature() for _ in range(20)]
        self.init_ui()
        self.start_data_update_thread()

    def init_ui(self):
        self.root = Tk()
        self.root.title("Dynamic Display")
        self.root.geometry("600x400")

        self.canvas = Canvas(self.root, width=600, height=300)
        self.canvas.pack()

        self.label = Label(self.root, text="Temperature")
        self.label.pack()

        self.button = Button(self.root, text="Go", command=self.update_chart)
        self.button.pack()

    def start_data_update_thread(self):
        self.data_thread = threading.Thread(target=self.update_data_continuously)
        self.data_thread.daemon = True
        self.data_thread.start()

    def update_data_continuously(self):
        while True:
            self.values.pop(0)
            self.values.append(self._generate_random_temperature())
            self.draw_chart()
            time.sleep(0.5)

    def _generate_random_temperature(self):
        normalized_value = random.random()
        temperature_range = self.base_max - self.base_min
        temperature = normalized_value * temperature_range + self.base_min
        return temperature

    def draw_chart(self):
        self.canvas.delete("line")
        x_start = 50
        x = x_start

        for i in range(len(self.values)):
            rect_height = (self.values[i] - self.base_min) / (self.base_max - self.base_min) * 250
            if i > 0:
                self.canvas.create_line(prev_x + 12.5, prev_y, x + 12.5, 250 - rect_height, fill="red", tag="line")
            prev_x, prev_y = x, 250 - rect_height
            x += 45

    def update_chart(self):
        messagebox.showinfo("Message", "This button is not functional in dynamic mode.")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    data_series = DisplayDynamicDataSeries()
    data_series.run()
