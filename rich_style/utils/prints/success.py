from ...core.combine_text import combine_text
from ...colors.presets import presets
from ...styles.bold import bold

_SUCCESS_COLOR = presets.bright_green

def success(*text: str, sep: str = " ", end: str = "\n", file=None, flush: bool = False) -> None:
    """Prints a success message."""
    
    combined_text = combine_text(*text, separator=sep)
    message = f"{_SUCCESS_COLOR('SUCC')} {combined_text}"
    print(bold(message), end=end, file=file, flush=flush)
