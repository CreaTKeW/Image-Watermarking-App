import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.dialogs.colorchooser import ColorChooserDialog
from ttkbootstrap.dialogs.dialogs import FontDialog
from ttkbootstrap.constants import *

class Settings:
    def __init__(self, parent, app_logic):
        self.app_logic = app_logic
        self.top = ttk.Toplevel(parent)
        self.top.title('Settings')
        self.top.place_window_center()
        self.top.focus_set()
        self.top.grab_set()

        self.preview_style_name = 'ColorPreview.TFrame'
        if self.app_logic.color is None:
            ttk.Style().configure(self.preview_style_name, background='#ffffff')

        self.top.rowconfigure(0, weight=1)
        self.top.columnconfigure(0, weight=1)
        mainframe = ttk.Frame(self.top, padding='10 10')
        mainframe.rowconfigure(0, weight=1)
        for i in range(2):
            mainframe.columnconfigure(i, weight=1)

        color_button = ttk.Button(mainframe, text='Text Color', command=self.color_dialog, style=(LIGHT, OUTLINE))
        font_button = ttk.Button(mainframe, text='Text Font', command=self.font_dialog, style=(LIGHT, OUTLINE))
        self.color_preview = ttk.Frame(mainframe, width=100, height=50, relief='ridge', borderwidth=2, style=self.preview_style_name)
        self.font_preview = ttk.Label(mainframe, text='Hello World!', font=self.app_logic.tk_font)
        mark_menu_button = ttk.Menubutton(mainframe, text='Watermark placement', style='Light.Outline.TMenubutton')
        apply_button = ttk.Button(mainframe, text='Apply', command=self.app_logic.apply_settings, style=INFO)
        cancel_button = ttk.Button(mainframe, text='Cancel', command=self.cancel, style=INFO)

        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        color_button.grid(column=0, row=0, sticky=(W, E), padx=(0, 5), pady=(10, 0))
        self.color_preview.grid(column=1, row=0,sticky=(W, E), padx=(5, 5), pady=(10, 0))
        self.font_preview.grid(column=1, row=1, padx=(5, 5), pady=(10, 0))
        font_button.grid(column=0, row=1, sticky=(W, E), padx=(0, 5), pady=(10, 0))
        mark_menu_button.grid(column=0, row=2, columnspan=2, sticky=(W, E), padx=(0, 5), pady=(10, 0))
        apply_button.grid(column=0, row=3, sticky=(W, E), padx=(0, 5), pady=(10, 0))
        cancel_button.grid(column=1, row=3, sticky=(W, E), padx=(5, 0), pady=(10, 0))

        mark_menu = tk.Menu(mark_menu_button)
        placement_options = ['bottom-left', 'top-left', 'center', 'bottom-right', 'top-right']
        self.option_var = tk.StringVar()
        self.option_var.set('bottom-left')
        for option in placement_options:
            mark_menu.add_radiobutton(label=option, value=option, variable=self.option_var)
        mark_menu_button['menu'] = mark_menu

    def color_dialog(self):
        cd = ColorChooserDialog()
        cd.show()

        colors = cd.result
        if colors:
            self.app_logic.color = colors
            self.update_color_preview(colors.hex)
        self.top.grab_set()

    def font_dialog(self):
        fd = FontDialog()
        fd.show()

        font = fd.result
        if font:
            self.app_logic.font = font
            self.font_preview.config(font=font)
        self.top.grab_set()

    def apply_settings(self):
        self.top.grab_release()
        self.top.destroy()

    def cancel(self):
        self.top.grab_release()
        self.top.destroy()

    def update_color_preview(self, color):
        ttk.Style().configure(self.preview_style_name, background=color)