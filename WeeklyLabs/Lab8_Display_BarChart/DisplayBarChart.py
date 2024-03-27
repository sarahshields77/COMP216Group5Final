from tkinter import *
from tkinter import messagebox

class DisplayBarChart:
    def __init__(self, base_min=18, base_max=21):
        self.base_min = base_min
        self.base_max = base_max
        self.init_ui()

    def init_ui(self):
        self.root = Tk()
        self.root.title("Lab 8")
        self.root.geometry("400x400")

        self.canvas = Canvas(self.root, width=400, height=320)
        self.canvas.pack()

        self.coord = 160, 70, 240, 300
        self.canvas.create_rectangle(self.coord, width="2", fill="white")

        self.canvas.create_text(200, 20, font="Arial 14", text="Server Room Temperature (18°C - 21°C)")
        self.canvas.create_text(140, 300, font="Arial 14", text=self.base_min)
        self.canvas.create_text(140, 70, font="Arial 14", text=self.base_max)
        self.canvas.create_text(140, 223, font="Arial 14", text="19")
        self.canvas.create_text(140, 147, font="Arial 14", text="20")

        self.entry = Entry(self.root)
        self.entry.pack(pady=(0, 15), ipady=(2))

        self.button = Button(self.root, text="Update Bar", bg="lightgrey", command=self.update_bar)
        self.button.pack(ipadx=(2), ipady=(2))
    
    def update_bar(self):
        # get input temp and check if valid
        new_temp = float(self.entry.get())
        if not self.base_min <= new_temp <= self.base_max:
            messagebox.showinfo("Error", "Invalid Temperature.")
            return
        
        # get height of new bar based on temperature input
        temp_range = self.base_max - self.base_min
        max_height = 230
        new_height = 300 - (((new_temp - self.base_min) / temp_range) * max_height)

        # new coord using new height
        new_coord = self.coord[:1] + (new_height,) + self.coord[2:]

        self.canvas.delete("bar")
        self.canvas.create_rectangle(new_coord, width="2", fill="lightgrey", tags="bar")

    def run(self):
        self.root.mainloop()
    
if __name__ == "__main__":
    bar_chart = DisplayBarChart()
    bar_chart.run()