import random, os, textwrap
from PIL import Image, ImageFont, ImageDraw

"""
from fbapp.models import Content, Gender


def find_content(gender):
    contents = Content.query.filter(Content.gender == Gender[gender]).all()
    return random.choice(contents)
"""


class OpenGraphImage:
    def __init__(self, uid, first_name, description):
        self.location = self._location(uid)
        background = self.base()
        self.print_on_img(background, first_name.capitalize(), 70, 50)

        sentences = textwrap.wrap(description, width=60)
        current_h, pad = 180, 10
        for sentence in sentences:
            w, h = self.print_on_img(background, sentence, 40, current_h)
            current_h += h + pad

        background.show(self._path(uid))

    @staticmethod
    def _path(uid):
        return os.path.join('static', 'tmp', '{}.jpg'.format(uid))

    @staticmethod
    def _location(uid):
        return 'tmp/{}.jpg'.format(uid)

    @staticmethod
    def base():
        img = Image.new('RGB', (1200, 630), '#18BC9C')
        return img

    @staticmethod
    def print_on_img(img, text, size, height):
        font = ImageFont.truetype(os.path.join('static', 'fonts', 'Arcon-Regular.otf'), size)
        draw = ImageDraw.Draw(img)
        w, h = draw.textsize(text, font)
        position = ((img.width - w) / 2, height)
        draw.text(position, text, (255, 255, 255), font=font)
        return w, h


description = """
    Toi, tu sais comment utiliser la console ! Jamais à court d'idées pour réaliser ton objectif, tu es déterminé-e et persévérant-e. Tes amis disent d'ailleurs volontiers que tu as du caractère et que tu ne te laisses pas marcher sur les pieds. Un peu hacker sur les bords, tu aimes trouver des solutions à tout problème. N'aurais-tu pas un petit problème d'autorité ? ;-)
    """
OpenGraphImage('Celine', description)
