from random import randint
from ..color import color

def random_color() -> color:
    return color(randint(0, 255), randint(0, 255), randint(0, 255))