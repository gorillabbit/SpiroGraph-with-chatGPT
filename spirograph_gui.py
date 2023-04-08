import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from spirograph_drawer import draw_animation, close_animation, close_plt


class SpirographGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Spirograph")
        self.anim = None

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

        self.R_label = tk.Label(self.master, text="大きな円のサイズ:")
        self.R_entry = tk.Entry(self.master, textvariable=R_var)
        self.r_label = tk.Label(self.master, text="小さな円のサイズ:")
        self.r_entry = tk.Entry(self.master, textvariable=r_var)
        self.p_label = tk.Label(self.master, text="ペン先の位置:")
        self.p_entry = tk.Entry(self.master, textvariable=p_var)
        self.angular_speed_ratio_label = tk.Label(self.master, text="回転の速度:")
        self.angular_speed_ratio_entry = tk.Entry(self.master, textvariable=angular_speed_ratio_var)
        self.submit_button = tk.Button(self.master, text="Draw", command=self.on_submit)

        self.R_label.grid(row=0, column=0, sticky="e")
        self.R_entry.grid(row=0, column=1, sticky="w")
        self.r_label.grid(row=1, column=0, sticky="e")
        self.r_entry.grid(row=1, column=1, sticky="w")
        self.p_label.grid(row=2, column=0, sticky="e")
        self.p_entry.grid(row=2, column=1, sticky="w")
        self.angular_speed_ratio_label.grid(row=4, column=0, sticky="e")
        self.angular_speed_ratio_entry.grid(row=4, column=1, sticky="w")
        self.submit_button.grid(row=0, column=2, rowspan=5, sticky=tk.NSEW)

        #閉じるときに、pltをクリアする
        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)

        # FigureとAxesを作成
        self.fig, self.ax = plt.subplots()

        #後でキャンバスが表示される空白
        self.empty_label = tk.Label(self.master, height=30, width=100)
        self.empty_label.grid(row=6, column=0, columnspan=4)

    def on_submit(self):
        R = int(self.R_entry.get())
        r = int(self.r_entry.get())
        p = int(self.p_entry.get())
        angular_speed_ratio = float(self.angular_speed_ratio_entry.get()) 

        if self.anim:
            self.canvas.get_tk_widget().destroy()

        self.anim = draw_animation(self.fig, R, r, p, angular_speed_ratio)

        # キャンバスを作成し、GUIに追加
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.get_tk_widget().grid(column=0, row=6, columnspan=4)

        self.canvas.draw()

    def on_closing(self):
        close_plt()
        self.master.destroy()

def main():
    root = tk.Tk()
    gui = SpirographGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()