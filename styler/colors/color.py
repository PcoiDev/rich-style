from dataclasses import dataclass
from ..enums.layers import layers

@dataclass(slots=True, frozen=True)
class color:
    r: int
    g: int
    b: int

    def __post_init__(self):
        object.__setattr__(self, 'r', max(0, min(255, self.r)))
        object.__setattr__(self, 'g', max(0, min(255, self.g)))
        object.__setattr__(self, 'b', max(0, min(255, self.b)))

    def __str__(self) -> str:
        return f"RGB({self.r}, {self.g}, {self.b})"

    def to_tuple(self) -> tuple[int, int, int]:
        return (self.r, self.g, self.b)

    def to_hex(self) -> str:
        return f"#{self.r:02x}{self.g:02x}{self.b:02x}"

    def to_template(self, layer: layers = layers.FOREGROUND) -> str:
        r, g, b = self.r, self.g, self.b

        ANSI_TEMPLATE = {
            layers.FOREGROUND: "\033[38;2;{r};{g};{b}m{{}}\033[0m",
            layers.BACKGROUND: "\033[48;2;{r};{g};{b}m{{}}\033[0m",
            layers.FULL: "\033[38;2;{r};{g};{b};48;2;{r};{g};{b}m{{}}\033[0m"
        }

        return ANSI_TEMPLATE[layer].format(r=r, g=g, b=b)

    def __call__(self, text: str, layer: layers = layers.FOREGROUND) -> str:
        template = self.to_template(layer)
        return template.format(text)