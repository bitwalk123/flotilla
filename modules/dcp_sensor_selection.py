import tkinter as tk

from modules.features import Features
from widgets.scrollable_frame import ScrollableFrame


class DCPSensorSelection(tk.Frame):
    def __init__(self, parent, features: Features):
        super().__init__(parent)
        self.features = features
        self.pack(fill=tk.BOTH, expand=True)
        self.init_ui()

    def init_ui(self):
        canvas = tk.Canvas(self, background='white')
        area_check = tk.Frame(canvas)

        hbar = tk.Scrollbar(self, orient=tk.HORIZONTAL)
        hbar.config(command=canvas.xview)
        hbar.pack(side=tk.BOTTOM, fill=tk.X)
        vbar = tk.Scrollbar(self, orient=tk.VERTICAL)
        vbar.config(command=canvas.yview)
        vbar.pack(side=tk.RIGHT, fill=tk.Y)

        canvas.create_window(0, 0, window=area_check, anchor=tk.NW)
        canvas.pack(fill=tk.BOTH, expand=True)
        canvas.update_idletasks()

        for j, step in enumerate(self.features.getSteps()):
            for i, sensor in enumerate(self.features.getSensors()):
                check = tk.Checkbutton(area_check, relief='raised')
                check.grid(row=i, column=j)
