import ttkbootstrap as ttk
from src.core.logic import Logic
from ttkbootstrap.constants import *

class App:
    def __init__(self, root):
        self.root = root
        root.title('Markapp')
        self.app_logic = Logic(self)

        mainframe = ttk.Frame(root, padding='10 10')
        root.rowconfigure(0, weight=1)
        root.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        for i in range(4):
            mainframe.columnconfigure(i, weight=1)

        self.image_path = self.app_logic.image_path
        self.image_label = ttk.Label(mainframe)

        if self.image_path:
            self.app_logic.display_image(str(self.image_path))

        water_label = ttk.Label(mainframe, text='Text to add: ')
        self.watermark_text_entry = ttk.Entry(mainframe)

        water_label.config(font=('Arial', 18))
        self.watermark_text_entry.config(font=('Arial', 18))
        ttk.Style().configure("TButton", padding=6, relief="flat", font=('Arial', 16))
        ttk.Style().configure('TMenubutton', padding=6, relief="flat", font=('Arial', 16))
        ttk.Style().configure('TMenubutton', padding=6, relief="flat", font=('Arial', 16))

        file_button = ttk.Button(mainframe, text='Choose image', command=self.app_logic.open_file, bootstyle=(INFO, OUTLINE))
        add_watermark_button = ttk.Button(mainframe, text='Add watermark', command=self.app_logic.add_watermark, bootstyle=(INFO, OUTLINE))
        save_image_button = ttk.Button(mainframe, text='Save changes', command= lambda : self.app_logic.save_image(), bootstyle=(INFO, OUTLINE))
        watermark_settings_button = ttk.Button(mainframe, text='Settings', command=self.app_logic.settings_window, bootstyle=(INFO, OUTLINE))

        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.image_label.grid(column=0, row=0, columnspan=4, pady=(0, 10))
        water_label.grid(column=0, row=1, sticky=W)
        self.watermark_text_entry.grid(column=0, row=2, columnspan=4, sticky=(W, E))
        file_button.grid(column=0, row=3, sticky=(W, E), padx=(0, 5), pady=(10, 0))
        add_watermark_button.grid(column=1, row=3, sticky=(W, E), padx=(0, 5), pady=(10, 0))
        save_image_button.grid(column=2, row=3, sticky=(W, E), padx=(0, 5), pady=(10, 0))
        watermark_settings_button.grid(column=3, row=3, sticky=(W, E), padx=(0, 5), pady=(10, 0))

        self.root.place_window_center()
