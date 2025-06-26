from ...core.combine_text import combine_text
from ...colors.presets import presets

_WARNING_COLOR = presets.orange

def warn(*text: str) -> None:
    """Prints a warning message in yellow color."""

    combined_text = combine_text(*text)
    print(_WARNING_COLOR(f"⚠︎ {combined_text}"))