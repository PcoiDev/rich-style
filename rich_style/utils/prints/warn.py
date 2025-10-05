from ...core.combine_text import combine_text
from ...colors.presets import presets
from ...styles.bold import bold

_WARN_COLOR = presets.bright_orange

def warn(*text: str, sep: str = " ", end: str = "\n", file=None, flush: bool = False) -> None:
    """Prints a warning message with color and bold formatting, supporting all print() arguments."""
    
    combined_text = combine_text(*text, separator=sep)
    message = f"{_WARN_COLOR('WARN')} {combined_text}"
    print(bold(message), end=end, file=file, flush=flush)
