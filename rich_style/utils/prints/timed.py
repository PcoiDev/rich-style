from ...colors.character_color_map import character_color_map
from ...core.combine_text import combine_text
from ...colors.presets import presets
from datetime import datetime

_COLOR = presets.royal_blue
_MAP = character_color_map({
    "[": _COLOR,
    "]": _COLOR,
}, default_color=presets.white)

def timed_print(*text: str, sep: str = " ", end: str = "\n", file=None, flush: bool = False) -> None:
    """Prints a message prefixed with the current time (H:M:S) on the left."""
    now = datetime.now()
    current_time_str = now.strftime("%H:%M:%S")

    combined_text = combine_text(*text, separator=sep)
    prefix = _MAP(f"[{current_time_str}]")

    print(f"{prefix} {combined_text}", end=end, file=file, flush=flush)
