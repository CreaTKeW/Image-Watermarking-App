import matplotlib.font_manager as fm
from matplotlib.font_manager import FontProperties
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
        self.tk_font = None
        self.font = None
        self.color = None
        self.text_positon = None

    def add_watermark_text(self, text: str,
                           image_path: str,
                           position: str,
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
                        font = ImageFont.load_default(size=30)

                bl_pos = (im.size[0] * 0.01, im.size[1] * 0.9)
                tl_pos = (im.size[0] * 0.01, im.size[1] * 0.01)
                center_pos = (im.size[0] * 0.5, im.size[1] * 0.5)
                br_pos = (im.size[0] * 0.9, im.size[1] * 0.9)
                tr_pos = (im.size[0] * 0.9, im.size[1] * 0.01)
                mark_pos = None

                position_dict = {
                    'bottom-left': bl_pos,
                    'top-left': tl_pos,
                    'center': center_pos,
                    'bottom-right': br_pos,
                    'top-right': tr_pos
                }

                try:
                    mark_pos = position_dict[position]
                except KeyError:
                    Messagebox.show_info(message='Position not found. Applying default position: bottom-left', title='Info', parent=self.main_root)
                    mark_pos = position_dict['bottom-left']

                draw.text(text=text, xy=mark_pos, font=font, fill=color)
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


        if self.color is None:
            watermark_color = self.color
        else:
            watermark_color = self.color.rgb

        self.watermarked_image = self.add_watermark_text(watermark_text, self.image_path, position=self.text_positon, font=self.font, color=watermark_color)
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
        self.tk_font = self.font
        self.color = self.color
        self.text_positon = self.settings.option_var.get()
        print(self.text_positon)

        self.settings.apply_settings()
        self.font = self.tkinter_font_to_pillow_font(self.tk_font)
        print(f'Successfully applied settings: color: {self.color}, font: {self.tk_font}, position: {self.text_positon}')

    def tkinter_font_to_pillow_font(self, tk_font):
        try:
            family = tk_font.actual('family')
            size = tk_font.actual('size')
            weight = tk_font.actual('weight')
            slant = tk_font.actual('slant')

            style = 'italic' if slant == 'italic' else 'normal'

            try:
                font_props = FontProperties(family=family, weight=weight, style=style, size=size)
                font_path = fm.findfont(font_props, fallback_to_default=True)

                pillow_font = ImageFont.truetype(font_path, size)
                return pillow_font

            except Exception as e:
                Messagebox.show_error(message=f"Error: Couldn't find font: '{family}' (weight: {weight}, style: {style}). Description: {e}")
                return ImageFont.load_default(size=30)

        except AttributeError:
            Messagebox.show_info(message='Font wasn\'t provided. Loading default font.')
            return ImageFont.load_default(size=30)
