from PIL import Image, ImageTk, ImageDraw, ImageFont, UnidentifiedImageError
from ttkbootstrap.dialogs.dialogs import Messagebox
from src.ui.settings_window import Settings
from tkinter import filedialog

class Logic:
    def __init__(self, app_instance):
        self.app_instance = app_instance
        self.main_root = app_instance.root

        self.image_path = '../resources/example.jpg'
        self.tk_image = None
        self.image_to_save = None
        self.watermarked_image = None
        self.image_width = 900
        self.image_height = 550

        self.settings = None
        self.font = None
        self.color = (255, 255, 255)

    def add_watermark_text(self, text: str,
                           image_path: str,
                           position: str = 'bottom-left',
                           font: ImageFont.ImageFont | None = None,
                           color: tuple[int, int, int] = (255, 255, 255)) -> Image.Image | None:

        try:
            with Image.open(image_path) as im:
                image_to_edit = im.copy()   #.convert("RGBA")
                draw = ImageDraw.Draw(image_to_edit)

                if font is None:
                    try:
                        font = ImageFont.truetype('arial.ttf', size=im.size[1] * 0.05)
                    except IOError:
                        font = ImageFont.load_default()

                # TODO: Replace this with a input argument using ttk.Menubutton
                bl_mark = (im.size[0] * 0.01, im.size[1] * 0.9)
                tl_mark = (im.size[0] * 0.01, im.size[1] * 0.01)
                center_mark = (im.size[0] * 0.5, im.size[1] * 0.5)

                if position == 'bottom-left':
                    mark_position = bl_mark

                draw.text(text=text, xy=mark_position, font=font, fill=color)
                return image_to_edit

        except IOError as e:
            print(f"I/O error: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None


    def open_file(self):
        filepath = filedialog.askopenfilename(
            title='Choose an image',
            filetypes=[('Image files', '*.jpg *.jpeg *.png *.bmp *.gif'), ('All files', '*.*')]
        )

        if filepath:
            try:
                self.display_image(filepath)
            except UnidentifiedImageError:
                print(f"Error. Invalid file type was passed.")

    def display_image(self, image_source):
        resampling_filter = Image.Resampling.LANCZOS

        try:
            if isinstance(image_source, str):
                image = Image.open(image_source)
                self.image_path = image_source
            elif isinstance(image_source, Image.Image):
                image = image_source
            else:
                Messagebox.show_error(message=f"Error: Invalid image source type: {type(image_source)}", title='Error', parent=self.main_root)
                return

            self.image_to_save = image.copy()
            resized_image = image.resize((self.image_width, self.image_height), resampling_filter)
            self.tk_image = ImageTk.PhotoImage(resized_image)
            self.app_instance.image_label.configure(image=self.tk_image)

        except FileNotFoundError:
            print(f"Error. Couldn't find file: {image_source}")
            Messagebox.show_error(message=f"File not found:\n{image_source}", title="File Error", parent=self.main_root)
        except UnidentifiedImageError:
            print(f"Error. Cannot identify image file: {image_source}")
            Messagebox.show_error(message=f"Cannot identify image file:\n{image_source}", title="File Error",
                                  parent=self.main_root)
        except Exception as e:
            print(f"Error displaying image: {e}")
            Messagebox.show_error(message=f"An error occurred while displaying the image.", title="Display Error",
                                  parent=self.main_root)

    def add_watermark(self):
        if not self.image_path:
             Messagebox.show_warning(message='Choose an image first.', title='Image not found.', parent=self.main_root, alert=True)
             return

        watermark_text = self.app_instance.watermark_text_entry.get()
        if not watermark_text:
            Messagebox.show_warning(message='Enter watermark text.', title='Text is null.', parent=self.main_root, alert=True)
            return

        self.watermarked_image = self.add_watermark_text(watermark_text, self.image_path, font=self.font, color=self.color)
        self.display_image(self.watermarked_image)

    def save_image(self):
        files = [('PNG files', '*.png'),
                 ('JPEG files', '*.jpg *.jpeg'),
                 ('BMP files', '*.bmp'),
                 ('GIF files', '*.gif'),
                 ('All files', '*.*')]

        filepath = filedialog.asksaveasfilename(title='Save as', filetypes=files, defaultextension='.png')
        if not filepath:
            return

        try:
            self.watermarked_image.save(filepath)
            Messagebox.ok(message=f'Your photo has been successfully saved.', title='Success', alert=False, parent=self.main_root)
        except AttributeError:
            Messagebox.show_error(message='Failed saving photo.', title='Failed', alert=True, parent=self.main_root)

    def settings_window(self):
        self.settings = Settings(self.main_root, self)

    def apply_settings(self):
        self.font = self.settings.font
        self.color = self.settings.color

        self.settings.apply_settings()
        print(f'Successfully applied settings: color: {self.color}, font: {self.font}')