from ..core.style import style
from ..colors.color import color
from ..enums.layers import layers

def background(color: color, *text, force_ansi: bool):
    """Applies a background color to the given text."""
    return style(color.to_template(layers.BACKGROUND))(*text, force_ansi)