import tkinter as tk
from tkinter import ttk

from modules.features import Features
from widgets.scrollable_frame import ScrollableFrame


class DCPSensorSelection(tk.Frame):
    def __init__(self, parent, features: Features):
        super().__init__(parent)
        self.features = features
        self.pack(fill=tk.BOTH, expand=True)

        area_check = ScrollableFrame(self)
        for j, step in enumerate(self.features.getSteps()):
            for i, sensor in enumerate(self.features.getSensors()):
                check = tk.Checkbutton(area_check.frame, relief='raised')
                check.grid(row=i, column=j)

        area_check.pack(fill=tk.BOTH, expand=True)

