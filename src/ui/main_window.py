import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk


class App:
    def __init__(self, root):
        root.title('Markapp')
        mainframe = ttk.Frame(root, padding='10 10')
        mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

        self.image_path = ''

        image = Image.open(self.image_path)
        self.image = ImageTk.PhotoImage(image, size=(1,1))
        image_label = ttk.Label(mainframe, image=self.image)
        image_label.grid(column=0, row=0)

        water_label = ttk.Label(mainframe, text='Text to add: ')
        water_label.grid(column=0, row=1, sticky=tk.W)

        watermark_text_entry = ttk.Entry(mainframe)
        watermark_text_entry.grid(column=0, row=2, columnspan=2, sticky=tk.W)

        file_button = ttk.Button(mainframe, text='Open image', command=self.open_file)
        file_button.grid(column=0, row=3, sticky=tk.W)

    def open_file(self):
        filepath = filedialog.askopenfilename()
