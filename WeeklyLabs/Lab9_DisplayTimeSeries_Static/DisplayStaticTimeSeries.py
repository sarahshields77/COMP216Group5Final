from tkinter import *
from tkinter import messagebox
import random

class DisplayStaticDataSeries:
    def __init__(self, base_min=18, base_max=21):
        self.base_min = base_min
        self.base_max = base_max
        # generate list of 20 random values using method from data generator class
        self.values = [self._generate_random_temperature() for _ in range(20)] 
        self.init_ui()

    def init_ui(self):
        self.root = Tk()
        self.root.title("Historical Data")
        self.root.geometry("600x400")

        self.canvas = Canvas(self.root, width=600, height=300)
        self.canvas.pack()

        # widgets for user input
        self.label = Label(self.root, text="Enter New Value:")
        self.label.place(x=20, y=320)

        self.entry = Entry(self.root)
        self.entry.place(x=130, y=320, width=100)

        self.button = Button(self.root, text="Update Chart", bg="lightgrey", command=self.update_chart)
        self.button.place(x=250, y=315)

        self.draw_chart()

    def _generate_random_temperature(self):
        # same method as in Lab 8 Temp Sensor that uses normalized value to calculate 
        # the temp. within the specified range
        normalized_value = random.random()  
        temperature_range = self.base_max - self.base_min
        temperature = normalized_value * temperature_range + self.base_min  
        return temperature

    def draw_chart(self):
        # clear canvas
        self.canvas.delete("all")

        # draw rectangles and lines
        rect_width = 25
        rect_gap = 20
        x_start = 50
        x = x_start

        for value in self.values:
            # draw bar chart
            rect_height = (value - self.base_min) / (self.base_max - self.base_min) * 250  # Scale the height
            self.canvas.create_rectangle(x, 250 - rect_height, x + rect_width, 250, fill="lightgreen")

            # draw line chart
            if x > x_start:
                self.canvas.create_line(prev_x + rect_width // 2, prev_y, x + rect_width // 2, 250 - rect_height, fill="red")

            # update x-coord for next rectangle
            prev_x, prev_y = x + rect_width // 2, 250 - rect_height
            x += rect_width + rect_gap

    def update_chart(self):
        # get input value and check if valid
        try:
            new_value = float(self.entry.get())
        except ValueError:
            messagebox.showinfo("Error", "Invalid Input: Please enter a valid number.")
            return

        if not self.base_min <= new_value <= self.base_max:
            messagebox.showinfo("Error", "Invalid Value: Please enter a value within the specified range.")
            return

        # update values list with new value
        self.values.pop(0)  # remove oldest value
        self.values.append(new_value)  # append new value

        # redraw chart
        self.draw_chart()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    data_series = DisplayStaticDataSeries()
    data_series.run()
