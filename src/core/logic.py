import sys
from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype('arial.ttf', 45)

def add_watermark_text(text, image_path):
    print(image_path)

    with Image.open(image_path) as im:
        image_to_edit = im.copy()
        draw = ImageDraw.Draw(image_to_edit)
        draw.multiline_text(text=text, xy=(15, 575), font=font)
        return image_to_edit
