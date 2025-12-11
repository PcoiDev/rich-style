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
        self.colors = {0.0: colors, 1.0: colors} if isinstance(colors, color) else colors
        self.start = start
        self.end = end
        self.type = type
        
    def _get_position_factor(self, x: int, y: int, max_x: int, max_y: int) -> float:
        if max_x <= 1:
            norm_x = self.start[0]
        else:
            norm_x = x / (max_x - 1)
            
        if max_y <= 1:
            norm_y = self.start[1]
        else:
            norm_y = y / (max_y - 1)
        
        if self.type == gradient_type.LINEAR:
            dx = self.end[0] - self.start[0]
            dy = self.end[1] - self.start[1]
            
            length_squared = dx * dx + dy * dy
            if length_squared == 0:
                return 0.0
            
            pdx = norm_x - self.start[0]
            pdy = norm_y - self.start[1]
            
            projection = (pdx * dx + pdy * dy) / length_squared
            
            # DEBUG PRINT
            if x == 0 and y in [0, max_y // 2, max_y - 1]:
                print(f"  -> projection={projection:.3f}, dx={dx}, dy={dy}, pdx={pdx:.3f}, pdy={pdy:.3f}")
            
            return max(0.0, min(1.0, projection))
        
        else:
            dx = norm_x - self.start[0]
            dy = norm_y - self.start[1]
            
            end_dx = self.end[0] - self.start[0]
            end_dy = self.end[1] - self.start[1]
            radius = sqrt(end_dx * end_dx + end_dy * end_dy)
            
            if radius == 0:
                return 0.0
            
            distance = sqrt(dx * dx + dy * dy)
            return max(0.0, min(1.0, distance / radius))
    
    def at(self, position: float) -> color:
        position = max(0.0, min(1.0, position))
        
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
                
                if end_pos == start_pos:
                    return start_color
                    
                factor = (position - start_pos) / (end_pos - start_pos)
                
                return color(
                    int(start_color.r + (end_color.r - start_color.r) * factor),
                    int(start_color.g + (end_color.g - start_color.g) * factor),
                    int(start_color.b + (end_color.b - start_color.b) * factor)
                )
            
        return self.colors[positions[0]] 
    
    def __call__(self, text: str, layer: layers = layers.TEXT) -> str:
        if not text:
            return text
            
        lines = text.split('\n')
        max_y = len(lines)
        max_x = max(len(line) for line in lines) if lines else 0
        
        if max_x == 0 or max_y == 0:
            return text
        
        styled_lines = []
        for y, line in enumerate(lines):
            styled_line_chars = []
            for x, char in enumerate(line):
                position_factor = self._get_position_factor(x, y, max_x, max_y)
                char_color = self.at(position_factor)
                styled_line_chars.append(char_color(char, layer))

            styled_lines.append("".join(styled_line_chars))
        
        return "\n".join(styled_lines)