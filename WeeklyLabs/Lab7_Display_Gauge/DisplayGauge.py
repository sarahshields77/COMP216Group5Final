from tkinter import *
from tkinter import messagebox

class DisplayGauge:
    def __init__(self, base_min=18, base_max=21):
        self.base_min = base_min
        self.base_max = base_max
        self.init_ui()

    def init_ui(self):
        self.root = Tk()
        self.root.title("Lab 7")
        self.root.geometry("400x300")

        self.canvas = Canvas(self.root, width=400, height=220)
        self.canvas.pack()

        self.start_angle = 180
        extent_angle = -180
        self.coord = 60, 60, 340, 340 
        self.canvas.create_arc(self.coord, start=self.start_angle, extent=extent_angle, width=3, fill="white")

        self.canvas.create_text(200, 20, font="Arial 18", text="Temperature in Server Room")
        self.canvas.create_text(40, 195, font="Arial 16", text=self.base_min)
        self.canvas.create_text(360, 195, font="Arial 16", text=self.base_max)
        self.canvas.create_text(125, 65, font="Arial 16", text="19")
        self.canvas.create_text(275, 65, font="Arial 16", text="20")

        self.entry = Entry(self.root)
        self.entry.pack(pady=(0, 15), ipady=(2))

        self.button = Button(self.root, text="Update Gauge", bg="lightgrey", command=self.update_gauge)
        self.button.pack(ipadx=(2), ipady=(2))
    
    def update_gauge(self):
        # get input temp and check if valid
        new_temp = float(self.entry.get())
        if not self.base_min <= new_temp <= self.base_max:
            messagebox.showinfo("Error", "Invalid Temperature.")
            return
        
        # get degree value based on temperature input
        angle_range = 180
        temp_range = self.base_max - self.base_min
        degrees = ((new_temp - self.base_min) / temp_range) * angle_range

        self.canvas.delete("needle")
        self.canvas.create_arc(self.coord, start=self.start_angle, extent=-degrees, width=3, fill="lightgrey", tags="needle")

    def run(self):
        self.root.mainloop()
    
if __name__ == "__main__":
    gauge = DisplayGauge()
    gauge.run()