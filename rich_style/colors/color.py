from dataclasses import dataclass
from ..enums import layers

_ANSI_TEMPLATE = {
    layers.TEXT: "\033[38;2;{r};{g};{b}m{{}}\033[39m",
    layers.BACKGROUND: "\033[48;2;{r};{g};{b}m{{}}\033[49m",
    layers.FULL: "\033[38;2;{r};{g};{b};48;2;{r};{g};{b}m{{}}\033[39m\033[49m"
}

@dataclass(slots=True, frozen=True)
class color:
    """Represents a color in RGB format with methods to convert to different formats."""
    r: int
    g: int
    b: int

    def __post_init__(self):
        """Ensure RGB values are within the range [0, 255]"""
        object.__setattr__(self, 'r', max(0, min(255, self.r)))
        object.__setattr__(self, 'g', max(0, min(255, self.g)))
        object.__setattr__(self, 'b', max(0, min(255, self.b)))

    def __str__(self) -> str:
        """Return a string representation of the color in RGB format."""
        return f"RGB({self.r}, {self.g}, {self.b})"
        
    def __repr__(self) -> str:
        """Return a detailed string representation for debugging."""
        return f"color(r={self.r}, g={self.g}, b={self.b})"


    def to_tuple(self) -> tuple[int, int, int]:
        """Return the color as an RGB tuple."""
        return (self.r, self.g, self.b)

    def to_hex(self) -> str:
        """Return the color in hexadecimal format."""
        return f"#{self.r:02x}{self.g:02x}{self.b:02x}"

    def to_template(self, layer: layers = layers.TEXT) -> str:
        """
        Return an ANSI escape code template for the color.
        The template can be used to format text with the specified color.
        """
        if layer not in _ANSI_TEMPLATE:
            raise ValueError(f"Unsupported layer for ANSI template: {layer}")

        return _ANSI_TEMPLATE[layer].format(r=self.r, g=self.g, b=self.b)

    def __call__(self, text: str, layer: layers = layers.TEXT) -> str:
        """Applies the ANSI color code to the given text for the specified layer."""
        template = self.to_template(layer)
        return template.format(text)