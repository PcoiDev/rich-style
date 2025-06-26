from ...core.combine_text import combine_text
from ...colors.presets import presets
from ...styles.bold import bold

_SUCCESS_COLOR = presets.bright_green

def success(*text: str) -> None:
    """Prints an success message."""

    combined_text = combine_text(*text)
    print(bold(f"{_SUCCESS_COLOR("SUCC")} {combined_text}"))
    