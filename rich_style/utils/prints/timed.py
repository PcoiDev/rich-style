from ...colors.character_color_map import character_color_map
from ...core.combine_text import combine_text
from ...colors.presets import presets
from ...styles.bold import bold

from datetime import datetime

_COLOR = presets.blue
_MAP = character_color_map({
    "[": _COLOR,
    "]": _COLOR,
})

def timed_print(*text: str):
    """Prints a message prefixed with the current time (H:M:S) on the left."""
    
    now = datetime.now()
    current_time_str = now.strftime("%H:%M:%S")

    combined_text = combine_text(*text)
    prefix = _MAP(f"[{current_time_str}]")

    print(f"{prefix} {combined_text}")
