from ...core.combine_text import combine_text
from ...colors.presets import presets

_INFO_COLOR = presets.blue

def info(*text: str) -> None:
    """Prints an informational message in blue color."""

    combined_text = combine_text(*text)
    print(_INFO_COLOR(f"ⓘ {combined_text}"))