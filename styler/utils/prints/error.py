from ...core.combine_text import combine_text
from ...colors.presets import presets
from ...styles.bold import bold

_ERROR_COLOR = presets.red

def error(*text: str):
    """Prints an error message in red color."""

    combined_text = combine_text(*text)
    print(bold(_ERROR_COLOR(f"⨉ {combined_text}")))