from ...core.combine_text import combine_text
from ...colors.presets import presets
from ...styles.bold import bold

_INFO_COLOR = presets.dodger_blue

def info(*text: str) -> None:
    """Prints an informational message."""

    combined_text = combine_text(*text)
    print(bold(f"{_INFO_COLOR("INFO")} {combined_text}"))
