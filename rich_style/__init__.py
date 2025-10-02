# colors
from .colors.character_color_map import character_color_map
from .colors.color import color
from .colors.gradient import gradient
from .colors.presets import presets

## parser
from .colors.parser.from_hsl import from_hsl
from .colors.parser.from_html import from_html
from .colors.parser.rainbow_text import rainbow_text
from .colors.parser.random_color import random_color

# enums
from .enums import gradient_type, layers

# styles
from .styles.background import background
from .styles.bold import bold
from .styles.bullet_list import bullet_list
from .styles.foreground import foreground
from .styles.italic import italic
from .styles.strikethrough import strikethrough
from .styles.underline import underline

# utils
from .utils.supports_ansi import supports_ansi

## prints
from .utils.prints.debug import debug
from .utils.prints.error import error
from .utils.prints.info import info
from .utils.prints.mutable import mutable_print
from .utils.prints.success import success
from .utils.prints.timed import timed_print
from .utils.prints.warn import warn

__init__ = [
    "character_color_map",
    "color"
    "gradient",
    "parser",

    "gradient_type",
    "layers",
    
    "from_hsl",
    "from_html",
    "rainbow_text",
    "random_color",

    "bold",
    "italic",
    "underline",
    "strikethrough",
    "bullet_list",

    "supports_ansi",

    "debug",
    "error",
    "info",
    "mutable_print",
    "success",
    "timed_print",
    "warn",
]