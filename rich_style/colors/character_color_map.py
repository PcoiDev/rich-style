from typing import Dict, Union, Optional, Callable

from .color import color
from .gradient import gradient
from ..enums import layers

def character_color_map(
    char_colors: Dict[str, Union[color, gradient]], 
    default_color: Optional[Union[color, gradient]] = None
) -> Callable[[str], str]:
    normalized_colors = {}
    
    for char, colorizer in char_colors.items():
        if not isinstance(colorizer, (color, gradient)):
            continue
            
        if char.isalpha():
            normalized_colors[char.lower()] = colorizer
            normalized_colors[char.upper()] = colorizer
        else:
            normalized_colors[char] = colorizer

    def color_text(text: str) -> str:
        if not text:
            return text
        
        lines = text.split('\n')
        max_y = len(lines)
        max_x = max(len(line) for line in lines) if lines else 0
        
        if max_x == 0 or max_y == 0:
            return text
        
        result = []
        for y, line in enumerate(lines):
            line_result = []
            for x, char in enumerate(line):
                colorizer = normalized_colors.get(char, default_color)
                
                if colorizer is None:
                    line_result.append(char)
                    continue
                    
                if isinstance(colorizer, gradient):
                    position_factor = colorizer._get_position_factor(x, y, max_x, max_y)
                    char_color = colorizer.at(position_factor)
                    line_result.append(char_color(char, layers.TEXT))
                else:
                    line_result.append(colorizer(char))
            
            result.append(''.join(line_result))
                
        return '\n'.join(result)
    
    return color_text