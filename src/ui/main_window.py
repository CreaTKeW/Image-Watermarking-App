import tkinter as tk
import sys
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk, UnidentifiedImageError
from src.core import logic


class App:
    def __init__(self, root):
        root.title('Markapp')

        # Setup mainframe as content frame holder
        mainframe = ttk.Frame(root, padding='10 10')
        mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

        # Keeps the layout responsive to width/height changes
        # The image size is fixed so it won't change
        for i in range(2):
            root.columnconfigure(i, weight=1)
            root.rowconfigure(i, weight=1)
            mainframe.columnconfigure(i, weight=1)
            mainframe.rowconfigure(i, weight=1)

        # Path to example photo from resources directory
        self.image_path = '../resources/example.jpg'

        # Image size // Width x Height
        self.image_width = 500
        self.image_height = 400

        # To display image TKinter requires to put it inside a Label
        self.image_label = ttk.Label(mainframe)
        self.image_label.grid(column=0, row=0, columnspan=2, pady=(0, 10))

        # A reference to PhotoImage constructor is required so it won't be deleted by garbage collector
        self.tk_image = None

        # if starting image path exists then pass it as a variable
        if self.image_path:
            self.display_image(str(self.image_path))

        water_label = ttk.Label(mainframe, text='Text to add: ')
        water_label.grid(column=0, row=1, sticky=tk.W)
        water_label.config(font=('Arial', 18))

        self.watermark_text_entry = ttk.Entry(mainframe)
        self.watermark_text_entry.grid(column=0, row=2, columnspan=2, sticky=(tk.W, tk.E))
        self.watermark_text_entry.config(font=('Arial', 18))

        # In order to change ttk button style we need to configure ttk.Style() class
        ttk.Style().configure("TButton", padding=6, relief="flat", font=('Arial', 16))

        file_button = ttk.Button(mainframe, text='Choose image', command=self.open_file)
        file_button.grid(column=0, row=3, sticky=(tk.W, tk.E))

        add_watermark_button = ttk.Button(mainframe, text='Add watermark', command=self.add_watermark)
        add_watermark_button.grid(column=1, row=3, sticky=(tk.W, tk.E))

        save_image_button = ttk.Button(mainframe, text='Save changes', command=self.save_image)
        save_image_button.grid(column=0, row=4, sticky=(tk.W, tk.E))

        watermark_settings_button = ttk.Button(mainframe, text='Settings')
        watermark_settings_button.grid(column=1, row=4, sticky=(tk.W, tk.E))

    def open_file(self):
        # Open file dialog and wait until a file is chosen
        filepath = filedialog.askopenfilename(
            title='Choose an image',
            filetypes=[('Image files', '*.jpg *.jpeg *.png *.bmp *.gif'), ('All files', '*.*')]
        )

        # Check if passed file is an image if not print error.
        if filepath:
            try:
                # Execute display_image func and pass new filepath as a variable
                self.display_image(filepath)
            except UnidentifiedImageError:
                print(f"Error. Invalid file type was passed.")

    def display_image(self, filepath):

        # Set the resampling filter to LANCZOS
        resampling_filter = Image.Resampling.LANCZOS

        try:
            # Create image variable by passing a filepath to a pillow Image class
            image = Image.open(filepath)

            # Resize the image and apply the filter
            resized_image = image.resize((self.image_width, self.image_height), resampling_filter)

            # Pass resized image to PhotoImage constructor to make the image compatible with GUI
            self.tk_image = ImageTk.PhotoImage(resized_image)

            # Finally apply the new image and store the path for future reference
            self.image_label.configure(image=self.tk_image)
            self.image_path = filepath

        except FileNotFoundError:
            print(f"Error. Couldn't find file: {filepath}")

        except AttributeError:
            resized_image = filepath.resize((self.image_width, self.image_height), resampling_filter)
            self.image_to_save = filepath
            self.tk_image = ImageTk.PhotoImage(resized_image)
            self.image_label.configure(image=self.tk_image)
            #self.image_path = filepath

    def add_watermark(self):
        if not self.image_path:
             messagebox.showwarning(title='Image not found.', message='Choose an image first.')
             return

        watermark_text = self.watermark_text_entry.get()
        if not watermark_text:
            messagebox.showwarning(title='Text is null.', message='Enter watermark text.')
            return

        self.watermarked_image = logic.add_watermark_text(watermark_text, self.image_path)
        self.display_image(self.watermarked_image)

    def save_image(self):
        # TODO: Implement save image method
        pass
        #self.watermarked_image.save()