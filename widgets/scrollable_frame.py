import tkinter as tk
from tkinter import ttk


class ScrollableFrame2(ttk.Frame):
    def __init__(self, container, bar_x=True, bar_y=True):
        super().__init__(container)
        self.canvas = tk.Canvas(self)
        self.scrollable_frame = ttk.Frame(self.canvas)
        self.scrollable_frame.bind(
            '<Configure>',
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox('all')
            )
        )
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor='nw')
        if bar_y:
            self.scrollbar_y = ttk.Scrollbar(self, orient='vertical', command=self.canvas.yview)
            self.scrollbar_y.pack(side=tk.RIGHT, fill='y')
            self.canvas.configure(yscrollcommand=self.scrollbar_y.set)
        if bar_x:
            self.scrollbar_x = ttk.Scrollbar(self, orient='horizontal', command=self.canvas.xview)
            self.scrollbar_x.pack(side=tk.BOTTOM, fill='x')
            self.canvas.configure(xscrollcommand=self.scrollbar_x.set)
        self.canvas.pack(side=tk.LEFT, fill='both', expand=True)


class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.Canvas(self)

        scrollbar_y = ttk.Scrollbar(self, orient='vertical', command=canvas.yview)
        scrollbar_x = ttk.Scrollbar(self, orient='horizontal', command=canvas.xview)
        self.frame = ttk.Frame(canvas)

        self.frame.bind(
            '<Configure>',
            lambda e: canvas.configure(
                scrollregion=canvas.bbox('all')
            )
        )

        canvas.create_window((0, 0), window=self.frame, anchor='nw')

        canvas.configure(yscrollcommand=scrollbar_y.set)
        canvas.configure(xscrollcommand=scrollbar_x.set)

        canvas.grid(row=0, column=0)
        scrollbar_y.grid(row=0, column=1, sticky=tk.N + tk.S)
        scrollbar_x.grid(row=1, column=0, sticky=tk.W+tk.E)
        container.columnconfigure(0, weight=1)
        container.rowconfigure(0, weight=1)