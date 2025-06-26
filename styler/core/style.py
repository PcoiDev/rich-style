from .supports_ansi import supports_ansi
from .combine_text import combine_text

supports_ansi = supports_ansi()

class style():
    def __init__(self, template: str):
        self.template = template
    
    def __call__(self, *text, force_ansi: bool = False):
        return self.format(combine_text(*text), force_ansi)
    
    def format(self, text: str, force_ansi: bool) -> str:
         if not supports_ansi and not force_ansi:
            return text
         
         return self.template.format(text)