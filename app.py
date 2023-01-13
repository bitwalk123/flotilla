import os
import tkinter as tk
from pathlib import Path
from tkinter import filedialog, ttk

from modules.dcp_sensor_selection import DCPSensorSelection
from modules.features import Features
from modules.read_csv import ReadCSV


class DCPCreator(tk.Frame):
    """DCP creator with the CSV file exported from the fleet analysis tool
    """
    __version__ = '0.1.5'
    __version_minor__ = '20230113'

    # directory location
    opendir: str = str(Path.home())

    # image/icon location
    imgdir = 'images'

    notebook: ttk.Notebook = None
    reader: ReadCSV = None
    features: Features = None

    def __init__(self, master: tk.Tk = None):
        super().__init__(master)
        self.master = master
        self.pack()
        # self.grid()
        master.title('DCP Creator')
        master.geometry('1000x800')
        master.iconbitmap(default=os.path.join(self.imgdir, 'logo.ico'))

        self.init_ui()

    def init_ui(self):
        # menubar
        menubar = tk.Menu(self)
        self.master.config(menu=menubar)
        # File
        menu_file = tk.Menu(menubar, tearoff=False)
        menu_file.add_command(label='Open', command=self.menu_open_file_clicked, accelerator='Ctrl+O')
        menu_file.bind_all('<Control-o>', self.menu_open_file_clicked)
        menu_file.add_separator()
        menu_file.add_command(label='Exit', command=self.master.destroy)
        menubar.add_cascade(label='File', menu=menu_file)

    def main_ui(self):
        """Main UI
        """
        print('SENSORS :', self.features.getSensors())
        print('STEPS   :', self.features.getSteps())
        print('STATS   :', self.features.getStats())
        if self.features.isOESExists():
            print('SENSORS (OES) :', self.features.getOESSensors())
            print('STEPS   (OES) :', self.features.getOESSteps())
            print('STATS   (OES) :', self.features.getOESStats())

        if self.notebook is not None:
            self.notebook.destroy()

        self.notebook = ttk.Notebook(self.master)
        self.notebook.pack(expand=True, fill='both')
        #self.notebook.grid()

        # tab_one = tk.Frame(notebook)
        page = {
            # 'summary': DCPSummary(self.features),
            'sensors': DCPSensorSelection(self.notebook, self.features),
            # 'recipe': DCPStepValueSetting(self.features),
            # 'stats': DCPStats(self.features),
        }

        self.notebook.add(page['sensors'], text='Selection', underline=0)



    # _/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_
    # handler for mouse click

    def menu_open_file_clicked(self, event=None):
        """Data Reader in CSV format, which is exported from main application
        """
        filename = filedialog.askopenfilename(
            title='Select CSV file in Zip format',
            filetypes=[("Zip", '.zip')],
            initialdir=self.opendir
        )
        if len(filename) == 0:
            return
        self.opendir = os.path.dirname(filename)
        self.reader = ReadCSV(filename)
        self.features = self.reader.read()
        self.main_ui()


def main():
    root = tk.Tk()
    app = DCPCreator(master=root)
    app.mainloop()


if __name__ == "__main__":
    main()
