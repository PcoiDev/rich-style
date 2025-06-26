from typing import Dict, Union, Optional, Callable

from .color import color
from .gradient import gradient

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
        total_lines = len(lines)
        
        result = []
        for y, line in enumerate(lines):
            line_result = []
            for x, char in enumerate(line):
                colorizer = normalized_colors.get(char, default_color)
                
                if colorizer is None:
                    line_result.append(char)
                    continue
                    
                if isinstance(colorizer, gradient):
                    color_factor = y / (total_lines - 1) if total_lines > 1 else 0
                    color = colorizer.at(color_factor)
                    line_result.append(color(char))
                else:
                    line_result.append(colorizer(char))
            
            result.append(''.join(line_result))
                
        return '\n'.join(result)
    
    return color_text