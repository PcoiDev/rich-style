from styler.core.style import style
from ..colors.color import color
from ..enums.layers import layers

def foreground(color: color, *text, force_ansi: bool):
    return style(color.to_template(layers.FOREGROUND))(*text, force_ansi)