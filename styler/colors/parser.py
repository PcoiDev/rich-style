from typing import List, Union, overload
from random import randint, choice

from .color import color
from .gradient import gradient

@overload
def from_rgb(r: int, g: int, b: int) -> color: ...

def from_rgb(r: int, g: int, b: int) -> color:
    return color(r, g, b)

def from_html(hex_code: str) -> color:
    hex_code = hex_code.lstrip('#')
    hex_code = ''.join(c * 2 for c in hex_code) if len(hex_code) == 3 else hex_code
    return color(*(int(hex_code[i:i+2], 16) for i in (0, 2, 4)))

def from_hsl(h: float, s: float, l: float) -> color:
    h = h % 360 / 360
    q = l * (1 + s) if l < 0.5 else l + s - l * s
    p = 2 * l - q
    
    def hue_rgb(t: float) -> float:
        t = t % 1
        if t < 1/6: return p + (q - p) * 6 * t
        if t < 1/2: return q
        if t < 2/3: return p + (q - p) * (2/3 - t) * 6
        return p

    return color(*(int(hue_rgb(h + i) * 255) for i in (1/3, 0, -1/3)))

@overload
def random_color(colors: List[color] = None) -> color: ...

@overload
def random_color(colors: List[Union[color, gradient]] = None) -> Union[color, gradient]: ...

def random_color(colors = None):
    if not colors:
        return color(*(randint(0, 255) for _ in range(3)))
    return choice(colors)