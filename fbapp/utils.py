import os
import random
import textwrap

from PIL import Image, ImageFont, ImageDraw

from fbapp.models import Content, Gender


def find_content(gender):
    contents = Content.query.filter(Content.gender == Gender[gender]).all()
    return random.choice(contents)


class OpenGraphImage:
    def __init__(self, uid, first_name, description):
        background = self.base()
        self.location = self._location(uid)
        self.print_on_img(background, first_name.capitalize(), 70, 50)

        sentences = textwrap.wrap(description, width=60)
        current_h, pad = 180, 10
        for sentence in sentences:
            w, h = self.print_on_img(background, sentence, 40, current_h)
            current_h += h + pad


    @staticmethod
    def base():
        img = Image.new('RGB', (1200, 630), '#18BC9C')
        return img

    @staticmethod
    def print_on_img(img, text, size, height):
        font = ImageFont.truetype(os.path.join('fbapp', 'static', 'fonts', 'Arcon-Regular.otf'), size)
        draw = ImageDraw.Draw(img)
        w, h = draw.textsize(text, font)
        position = ((img.width - w) / 2, height)
        draw.text(position, text, (255, 255, 255), font=font)
        return w, h

    @staticmethod
    def _path(uid):
        return os.path.join('static', 'tmp', '{}.jpg'.format(uid))

    @staticmethod
    def _location(uid):
        return 'tmp/{}.jpg'.format(uid)


