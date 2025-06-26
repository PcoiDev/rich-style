from ...core.combine_text import combine_text
from ...colors.presets import presets

_SUCCESS_COLOR = presets.bright_green

def success(*text: str) -> None:
    """Prints a success message in green color."""

    combined_text = combine_text(*text)
    print(_SUCCESS_COLOR(f"✓ {combined_text}"))