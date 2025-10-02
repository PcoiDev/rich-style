from random import choice, random, randint
from typing import List, Union, Optional

from ..color import color
from ..gradient import gradient

def random_color(colors: Optional[List[Union[color, gradient]]] = None) -> color:
    if not colors or colors == None or len(colors) == 0:
        return color(randint(0, 255), randint(0, 255), randint(0, 255))
            
    chosen_item = choice(colors)

    if isinstance(chosen_item, color):
        return chosen_item
    else:
        return chosen_item.color_at(random())