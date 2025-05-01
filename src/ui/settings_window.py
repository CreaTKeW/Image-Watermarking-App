import tkinter as tk
import ttkbootstrap as ttk
#from tkinter import filedialog, messagebox
from ttkbootstrap.dialogs.colorchooser import ColorChooserDialog
from ttkbootstrap.dialogs.dialogs import FontDialog
from ttkbootstrap.constants import *

class Settings:
    def __init__(self, parent):
        self.top = tk.Toplevel(parent)
        self.top.title('Settings')

        #self.top.geometry('400x300')
        self.top.grab_set()

        mainframe = ttk.Frame(self.top, padding='10 10')
        mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

        self.top.rowconfigure(0, weight=1)
        self.top.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)

        for i in range(2):
            mainframe.columnconfigure(i, weight=1)

        color_button = ttk.Button(mainframe, text='Text Color', command= lambda: self.color_dialog())
        font_button = ttk.Button(mainframe, text='Text Font', command=lambda: self.font_dialog())
        apply_button = ttk.Button(mainframe, text='Apply', command=self.apply_settings)
        cancel_button = ttk.Button(mainframe, text='Cancel', command=self.cancel)

        color_button.grid(column=0, row=0, sticky=(tk.W, tk.E), padx=(0, 5), pady=(10, 0))
        font_button.grid(column=0, row=1, sticky=(tk.W, tk.E), padx=(0, 5), pady=(10, 0))
        apply_button.grid(column=0, row=2, sticky=(tk.W, tk.E), padx=(0, 5), pady=(10, 0))
        cancel_button.grid(column=1, row=2, sticky=(tk.W, tk.E), padx=(5, 0), pady=(10, 0))


    def color_dialog(self):
        cd = ColorChooserDialog()
        cd.show()

        colors = cd.result
        return colors

    def font_dialog(self):
        fd = FontDialog()
        fd.show()

        font = fd.result
        return font

    def apply_settings(self):
        print("Successfully applied new settings")
        self.top.destroy()

    def cancel(self):
        self.top.destroy()