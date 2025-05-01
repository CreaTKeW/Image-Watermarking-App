import ttkbootstrap as ttk
from ttkbootstrap.dialogs.colorchooser import ColorChooserDialog
from ttkbootstrap.dialogs.dialogs import FontDialog
from ttkbootstrap.constants import *
from PIL import ImageFont

class Settings:
    def __init__(self, parent):
        self.top = ttk.Toplevel(parent)
        self.top.title('Settings')
        self.top.place_window_center()
        self.top.focus_set()
        self.top.grab_set()

        self.top.rowconfigure(0, weight=1)
        self.top.columnconfigure(0, weight=1)
        mainframe = ttk.Frame(self.top, padding='10 10')
        mainframe.rowconfigure(0, weight=1)
        for i in range(2):
            mainframe.columnconfigure(i, weight=1)

        color_button = ttk.Button(mainframe, text='Text Color', command=self.color_dialog, style=(LIGHT, OUTLINE))
        font_button = ttk.Button(mainframe, text='Text Font', command=self.font_dialog, style=(LIGHT, OUTLINE))
        apply_button = ttk.Button(mainframe, text='Apply', command=self.apply_settings, style=INFO)
        cancel_button = ttk.Button(mainframe, text='Cancel', command=self.cancel, style=INFO)

        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        color_button.grid(column=0, row=0, sticky=(W, E), padx=(0, 5), pady=(10, 0))
        font_button.grid(column=0, row=1, sticky=(W, E), padx=(0, 5), pady=(10, 0))
        apply_button.grid(column=0, row=2, sticky=(W, E), padx=(0, 5), pady=(10, 0))
        cancel_button.grid(column=1, row=2, sticky=(W, E), padx=(5, 0), pady=(10, 0))

        self.color = (255, 255, 255)
        self.font = ImageFont.truetype('arial.ttf', 18)

    def color_dialog(self):
        cd = ColorChooserDialog()
        cd.show()

        colors = cd.result
        if colors:
            self.color = colors.rgb

    def font_dialog(self):
        fd = FontDialog()
        fd.show()

        font = fd.result
        if font:
            self.font = font

    def apply_settings(self):
        print("Successfully applied new settings")
        self.top.grab_release()
        self.top.destroy()

    def cancel(self):
        self.top.grab_release()
        self.top.destroy()