from ...core.combine_text import combine_text
from ...colors.presets import presets
from ...styles.bold import bold

_DEBUG_COLOR = presets.yellow

def debug(*text: str) -> None:
    """Prints a debug message."""

    combined_text = combine_text(*text)
    print(bold(f"{_DEBUG_COLOR("DEBU")} {combined_text}"))
    