from ...core.combine_text import combine_text
from ...enums import gradient_type, layers
from ..gradient import gradient
from ..presets import presets

_GRADIENT_COLOR = gradient(
    {
        0: presets.red,
        1/8: presets.bright_orange,
        2/8: presets.yellow,
        3/8: presets.bright_green,
        4/8: presets.cyan,
        5/8: presets.deep_blue,
        6/8: presets.violet,
        7/8: presets.magenta,
        1: presets.pink,
    },
    start=(0, 0.5),
    end=(1, 0.5),
    type=gradient_type.LINEAR
)

def rainbow_text(*text: str) -> str:
    """Returns a rainbow-colored text string."""
    combined_text = combine_text(*text)
    return _GRADIENT_COLOR(combined_text, layer=layers.TEXT)
