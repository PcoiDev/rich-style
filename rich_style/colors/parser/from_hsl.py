from ..color import color

def from_hsl(h: float, s: float, l: float) -> color:
    """Converts HSL color values to an RGB color object."""
    h = h % 360 / 360
    q = l * (1 + s) if l < 0.5 else l + s - l * s
    p = 2 * l - q
    
    def hue_rgb(t: float) -> float:
        """Helper function to convert hue to RGB component."""
        t = t % 1
        
        if t < 1/6:
            return p + (q - p) * 6 * t
        
        if t < 1/2:
            return q
        
        if t < 2/3:
            return p + (q - p) * (2/3 - t) * 6
        
        return p

    return color(*(int(hue_rgb(h + i) * 255) for i in (1/3, 0, -1/3)))