from ...core.combine_text import combine_text
from ...colors.presets import presets
from ...styles.bold import bold

_INFO_COLOR = presets.dodger_blue

def info(*text: str, sep: str = " ", end: str = "\n", file=None, flush: bool = False) -> None:
    """Prints an informational message."""
    
    combined_text = combine_text(*text, separator=sep)
    message = f"{_INFO_COLOR('INFO')} {combined_text}"
    print(bold(message), end=end, file=file, flush=flush)
