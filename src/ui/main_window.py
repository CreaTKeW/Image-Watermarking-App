import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk

class App:
    def __init__(self, root):
        root.title('Markapp')
        mainframe = ttk.Frame(root, padding='10 10')
        mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        self.image_path = '../resources/example.jpg'

        # Fixed image size
        self.image_width = 500
        self.image_height = 400

        self.image_label = ttk.Label(mainframe)
        self.image_label.grid(column=0, row=0, columnspan=2, pady=(0, 10))
        self.tk_image = None

        if self.image_path:
            self.display_image(str(self.image_path))

        water_label = ttk.Label(mainframe, text='Text to add: ')
        water_label.grid(column=0, row=1, sticky=tk.W)
        water_label.config(font=('Arial', 18))

        self.watermark_text_entry = ttk.Entry(mainframe)
        self.watermark_text_entry.grid(column=0, row=2, columnspan=2, sticky=(tk.W, tk.E))
        self.watermark_text_entry.config(font=('Arial', 18))

        ttk.Style().configure("TButton", padding=6, relief="flat", font=('Arial', 16))

        file_button = ttk.Button(mainframe, text='Choose image', command=self.open_file)
        file_button.grid(column=0, row=3, sticky=(tk.W, tk.E))

        add_watermark_button = ttk.Button(mainframe, text='Add watermark', command=self.add_watermark)
        add_watermark_button.grid(column=1, row=3, sticky=(tk.W, tk.E))

        # Keep the elements inside the frame resizable, requires both methods for same button sizes
        mainframe.columnconfigure(0, weight=1)
        mainframe.columnconfigure(1, weight=1)

    def display_image(self, filepath):
        try:
            image = Image.open(filepath)
            resampling_filter = Image.Resampling.LANCZOS


            resized_image = image.resize((self.image_width, self.image_height), resampling_filter)
            self.tk_image = ImageTk.PhotoImage(resized_image)
            self.image_label.configure(image=self.tk_image)

            self.image_path = filepath

        except FileNotFoundError:
            print(f"Error. Couldn't find file: {filepath}")

    def open_file(self):
        filepath = filedialog.askopenfilename(
            title='Choose an image',
            filetypes=[('Image files', '*.jpg *.jpeg *.png *.bmp *.gif'), ('All files', '*.*')]
        )
        if filepath:
            self.display_image(filepath)

    def add_watermark(self):
        if not self.image_path:
             print("Choose an image first.")
             return

        watermark_text = self.watermark_text_entry.get()
        if not watermark_text:
            print("Enter watermark text.")
            return

        print(f"Adding watermark text: '{watermark_text}' to image: {self.image_path}")