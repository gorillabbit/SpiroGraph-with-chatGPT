import tkinter as tk
from tkinter import ttk
from spirograph_drawer import spirograph_theta, draw_spirograph_animation

class SpirographGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Spirograph Drawer")

        self.R_label = ttk.Label(self, text="R:")
        self.R_entry = ttk.Entry(self)
        self.r_label = ttk.Label(self, text="r:")
        self.r_entry = ttk.Entry(self)
        self.p_label = ttk.Label(self, text="p:")
        self.p_entry = ttk.Entry(self)
        self.angular_speed_ratio_label = ttk.Label(self, text="angular_speed_ratio:")
        self.angular_speed_ratio_entry = ttk.Entry(self)
        self.submit_button = ttk.Button(self, text="Submit", command=self.on_submit)

        self.R_label.grid(row=0, column=0)
        self.R_entry.grid(row=0, column=1)
        self.r_label.grid(row=1, column=0)
        self.r_entry.grid(row=1, column=1)
        self.p_label.grid(row=2, column=0)
        self.p_entry.grid(row=2, column=1)
        self.angular_speed_ratio_label.grid(row=4, column=0)
        self.angular_speed_ratio_entry.grid(row=4, column=1)
        self.submit_button.grid(row=5, column=0, columnspan=2)

    def on_submit(self):
        R = int(self.R_entry.get())
        r = int(self.r_entry.get())
        p = int(self.p_entry.get())
        angular_speed_ratio = float(self.angular_speed_ratio_entry.get())

        theta = spirograph_theta(R, r, angular_speed_ratio)
        draw_spirograph_animation(R, r, p, theta)

if __name__ == "__main__":
    app = SpirographGUI()
    app.mainloop()
