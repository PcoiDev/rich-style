from ..color import color

def from_html(hex_code: str) -> color:
    """
    Converts a hex color code to a color object.
    Supports both 3-digit and 6-digit hex codes.
    """

    hex_code = hex_code.lstrip('#')
    hex_code = ''.join(c * 2 for c in hex_code) if len(hex_code) == 3 else hex_code
    return color(*(int(hex_code[i:i+2], 16) for i in (0, 2, 4)))