import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
from spirograph_drawer import spirograph_theta, update, spirograph_xy


class SpirographGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Spirograph")

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

        self.R_label = tk.Label(self.master, text="R:")
        self.R_entry = tk.Entry(self.master, textvariable=R_var)
        self.r_label = tk.Label(self.master, text="r:")
        self.r_entry = tk.Entry(self.master, textvariable=r_var)
        self.p_label = tk.Label(self.master, text="p:")
        self.p_entry = tk.Entry(self.master, textvariable=p_var)
        self.angular_speed_ratio_label = tk.Label(self.master, text="angular_speed_ratio:")
        self.angular_speed_ratio_entry = tk.Entry(self.master, textvariable=angular_speed_ratio_var)
        self.submit_button = tk.Button(self.master, text="Draw", command=self.on_submit)

        self.R_label.grid(row=0, column=0)
        self.R_entry.grid(row=0, column=1)
        self.r_label.grid(row=1, column=0)
        self.r_entry.grid(row=1, column=1)
        self.p_label.grid(row=2, column=0)
        self.p_entry.grid(row=2, column=1)
        self.angular_speed_ratio_label.grid(row=4, column=0)
        self.angular_speed_ratio_entry.grid(row=4, column=1)
        self.submit_button.grid(column=0, row=4, columnspan=2)

        # FigureとAxesを作成
        self.fig, self.ax = plt.subplots()

        # キャンバスを作成し、GUIに追加
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.get_tk_widget().grid(column=0, row=5, columnspan=2)

    def on_submit(self):
        R = int(self.R_entry.get())
        r = int(self.r_entry.get())
        p = int(self.p_entry.get())
        angular_speed_ratio = float(self.angular_speed_ratio_entry.get())

        # スピログラフの描画
        self.draw_spirograph(R, r, p, angular_speed_ratio)

    def _clear(self):
        for item in self.canvas.get_tk_widget().find_all():
            print(item)
            #self.canvas.get_tk_widget().delete(item)
        
    def draw_spirograph(self, R, r, p, angular_speed_ratio):

        theta = spirograph_theta(R, r, angular_speed_ratio)
        x, y = spirograph_xy(R, r, p, theta)
        anim = FuncAnimation(self.fig, update, frames=range(1000), fargs=(R, r, p, x, y, theta), interval=50)
        # 最後に、キャンバスを更新
        self.canvas.draw()


def main():
    root = tk.Tk()
    gui = SpirographGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()