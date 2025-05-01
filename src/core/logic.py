from PIL import Image, ImageDraw, ImageFont

def add_watermark_text(text, image_path):
    with Image.open(image_path) as im:

        bl_mark = (im.size[0] * 0.01, im.size[1] * 0.9)
        tl_mark = (im.size[0] * 0.01, im.size[1] * 0.01)
        center_mark = (im.size[0] * 0.5, im.size[1] * 0.5)

        image_to_edit = im.copy()
        draw = ImageDraw.Draw(image_to_edit)

        try:
            font = ImageFont.truetype('arial.ttf', 45)
        except IOError:
            font = ImageFont.load_default()

        draw.multiline_text(text=text, xy=bl_mark, font=font)
        return image_to_edit

