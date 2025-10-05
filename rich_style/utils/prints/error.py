from ...core.combine_text import combine_text
from ...colors.presets import presets
from ...styles.bold import bold

_ERROR_COLOR = presets.red

def error(*text: str, sep: str = " ", end: str = "\n", file=None, flush: bool = False) -> None:
    """Prints an error message."""
    
    combined_text = combine_text(*text, separator=sep)
    message = f"{_ERROR_COLOR('ERRO')} {combined_text}"
    print(bold(message), end=end, file=file, flush=flush)
