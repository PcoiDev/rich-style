from ...core.combine_text import combine_text
from ...colors.presets import presets
from ...styles.bold import bold

_ERROR_COLOR = presets.red

def error(*text: str) -> None:
    """Prints an error message."""

    combined_text = combine_text(*text)
    print(bold(f"{_ERROR_COLOR("ERRO")} {combined_text}"))
    