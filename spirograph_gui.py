import tkinter as tk
from spirograph_drawer import spirograph_theta, draw_spirograph_animation

class SpirographGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Spirograph Drawer")

        # デフォルト値を設定
        default_R = 100
        default_r = 75
        default_p = 50
        default_angular_speed_ratio = 2

        # StringVarオブジェクトを作成し、デフォルト値を設定
        R_var = tk.StringVar(value=default_R)
        r_var = tk.StringVar(value=default_r)
        p_var = tk.StringVar(value=default_p)
        angular_speed_ratio_var = tk.StringVar(value=default_angular_speed_ratio)

        self.R_label = tk.Label(self, text="R:")
        self.R_entry = tk.Entry(self, textvariable=R_var)
        self.r_label = tk.Label(self, text="r:")
        self.r_entry = tk.Entry(self, textvariable=r_var)
        self.p_label = tk.Label(self, text="p:")
        self.p_entry = tk.Entry(self, textvariable=p_var)
        self.angular_speed_ratio_label = tk.Label(self, text="angular_speed_ratio:")
        self.angular_speed_ratio_entry = tk.Entry(self, textvariable=angular_speed_ratio_var)
        self.submit_button = tk.Button(self, text="Submit", command=self.on_submit)

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
        print(angular_speed_ratio)

        theta = spirograph_theta(R, r, angular_speed_ratio)
        draw_spirograph_animation(R, r, p, theta, angular_speed_ratio)

if __name__ == "__main__":
    app = SpirographGUI()
    app.mainloop()
