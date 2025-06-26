from typing import Dict, Union, Tuple

from .color import color
from ..enums.layers import layers
from ..enums.gradient_type import gradient_type

def sqrt(n: float, square: float=2) -> float:
    return pow(n, (1 / square))

class gradient:
    __slots__ = ('colors', 'start', 'end', 'gradient_type')

    def __init__(
        self,
        colors: Union[color, Dict[float, color]],
        start: Tuple[float, float] = (0.5, 0),
        end: Tuple[float, float] = (0.5, 1),
        gradient_type: gradient_type = gradient_type.LINEAR # type: ignore
    ):
        self.colors = {0: colors, 1: colors} if isinstance(colors, color) else colors
        self.start = start
        self.end = end
        self.gradient_type = gradient_type
        
    def _get_position_factor(self, x: int, y: int, max_x: int, max_y: int) -> float:
        if not (max_x or max_y):
            return 0
            
        norm_x = x / max_x if max_x else 0
        norm_y = y / max_y if max_y else 0
        
        if self.gradient_type == gradient_type.LINEAR:
            dx = self.end[0] - self.start[0]
            dy = self.end[1] - self.start[1]
            pdx = norm_x - self.start[0]
            pdy = norm_y - self.start[1]
            dot = dx * pdx + dy * pdy
            mag = dx * dx + dy * dy
            return max(0, min(1, dot / mag if mag else 0))
        
        dx = norm_x - self.start[0]
        dy = norm_y - self.start[1]
        radius = sqrt((self.end[0] - self.start[0]) ** 2 + (self.end[1] - self.start[1]) ** 2)
        return max(0, min(1, sqrt(dx * dx + dy * dy) / radius if radius else 0))
    
    def at(self, position: float) -> color:
        if position in self.colors:
            return self.colors[position]
            
        positions = sorted(self.colors)
        if position <= positions[0]:
            return self.colors[positions[0]]
        if position >= positions[-1]:
            return self.colors[positions[-1]]
            
        for i in range(len(positions) - 1):
            if positions[i] <= position <= positions[i + 1]:
                start_pos = positions[i]
                end_pos = positions[i + 1]
                start_color = self.colors[start_pos]
                end_color = self.colors[end_pos]
                factor = (position - start_pos) / (end_pos - start_pos)
                return color(
                    int(start_color.r + (end_color.r - start_color.r) * factor),
                    int(start_color.g + (end_color.g - start_color.g) * factor),
                    int(start_color.b + (end_color.b - start_color.b) * factor)
                )
    
    def __call__(self, text: str, layer: layers = layers.FOREGROUND) -> str:
        if not text:
            return text
            
        if len(text) == 1:
            return self.at(0)(text, layer)
            
        lines = text.split('\n')
        max_y = len(lines)
        max_x = max(len(line) for line in lines)
        
        x_range = max_x - 1
        y_range = max_y - 1
        
        return '\n'.join(
            ''.join(
                self.at(self._get_position_factor(x, y, x_range, y_range))(char, layer)
                for x, char in enumerate(line)
            )
            for y, line in enumerate(lines)
        )