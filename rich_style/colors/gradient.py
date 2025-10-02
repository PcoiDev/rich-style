from typing import Dict, Union, Tuple

from .color import color
from ..enums import gradient_type, layers

def sqrt(n: float, square: float = 2) -> float:
    return pow(n, (1 / square))

class gradient:
    __slots__ = ('colors', 'start', 'end', 'type')

    def __init__(
        self,
        colors: Union[color, Dict[float, color]],
        start: Tuple[float, float] = (0.5, 0),
        end: Tuple[float, float] = (0.5, 1),
        type: gradient_type = gradient_type.LINEAR
    ):
        """Initializes a gradient with specified colors, start and end positions, and gradient type."""
        self.colors = {0.0: colors, 1.0: colors} if isinstance(colors, color) else colors
        self.start = start
        self.end = end
        self.type = type
        
    def _get_position_factor(self, x: int, y: int, max_x: int, max_y: int) -> float:
        """Calculates the position factor based on the x and y coordinates."""
        if max_x <= 1 and max_y <= 1:
            return 0.0
            
        norm_x = x / (max_x - 1) if max_x > 1 else 0.0
        norm_y = y / (max_y - 1) if max_y > 1 else 0.0
        
        if self.type == gradient_type.LINEAR:
            dx = self.end[0] - self.start[0]
            dy = self.end[1] - self.start[1]
            pdx = norm_x - self.start[0]
            pdy = norm_y - self.start[1]
            
            dot = dx * pdx + dy * pdy
            mag_squared = dx * dx + dy * dy
            
            if mag_squared == 0:
                return 0.0
            
            return max(0.0, min(1.0, dot / mag_squared))
        
        dx = norm_x - self.start[0]
        dy = norm_y - self.start[1]
        
        radius = sqrt((self.end[0] - self.start[0]) ** 2 + (self.end[1] - self.start[1]) ** 2)
        
        if radius == 0:
            return 0.0
            
        return max(0.0, min(1.0, sqrt(dx * dx + dy * dy) / radius))
    
    def at(self, position: float) -> color:
        """Returns the color at a specific position in the gradient."""
        if position in self.colors:
            return self.colors[position]
            
        positions = sorted(self.colors.keys())
        
        if position <= positions[0]:
            return self.colors[positions[0]]
        if position >= positions[-1]:
            return self.colors[positions[-1]]
            
        for i in range(len(positions) - 1):
            start_pos = positions[i]
            end_pos = positions[i + 1]
            
            if start_pos <= position <= end_pos:
                start_color = self.colors[start_pos]
                end_color = self.colors[end_pos]
                
                # Avoid division by zero if start_pos and end_pos are identical
                if end_pos == start_pos:
                    return start_color
                    
                factor = (position - start_pos) / (end_pos - start_pos)
                
                # Linearly interpolate RGB components
                return color(
                    int(start_color.r + (end_color.r - start_color.r) * factor),
                    int(start_color.g + (end_color.g - start_color.g) * factor),
                    int(start_color.b + (end_color.b - start_color.b) * factor)
                )
            
        return self.colors[positions[0]] 
    
    def __call__(self, text: str, layer: layers = layers.TEXT) -> str:
        """Applies the gradient to the given text."""
        if not text:
            return text
            
        if len(text) == 1:
            return self.at(0.0)(text, layer)
            
        lines = text.split('\n')
        max_y = len(lines)
        max_x = 0
        for line in lines:
            if len(line) > max_x:
                max_x = len(line)
        
        styled_lines = []
        for y, line in enumerate(lines):
            styled_line_chars = []
            for x, char in enumerate(line):
                position_factor = self._get_position_factor(x, y, max_x, max_y)
                char_color = self.at(position_factor)
                styled_line_chars.append(char_color(char, layer))
                
            for x_pad in range(len(line), max_x):
                position_factor = self._get_position_factor(x_pad, y, max_x, max_y)
                char_color = self.at(position_factor)
                styled_line_chars.append(char_color(' ', layer))

            styled_lines.append("".join(styled_line_chars))
            
        return "\n".join(styled_lines)
