from random import choice, random, randint
from typing import List, Union, Optional

from ..color import color
from ..gradient import gradient

def random_color() -> color:
    return color(randint(0, 255), randint(0, 255), randint(0, 255))