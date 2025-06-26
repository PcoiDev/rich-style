from ...core.combine_text import combine_text
from ...colors.presets import presets
from ...styles.bold import bold

_WARN_COLOR = presets.bright_orange

def warn(*text: str) -> None:
    """Prints an warning message."""

    combined_text = combine_text(*text)
    print(bold(f"{_WARN_COLOR("WARN")} {combined_text}"))
    