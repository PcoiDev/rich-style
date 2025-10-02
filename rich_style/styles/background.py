from ..core.style import style
from ..colors.color import color
from ..enums import layers

def background(color: color, *text, force_ansi: bool = False):
    """Applies a foreground color to the given text."""
    return style(color.to_template(layers.BACKGROUND))(*text, force_ansi=force_ansi)