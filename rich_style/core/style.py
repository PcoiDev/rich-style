from ..utils.supports_ansi import supports_ansi
from .combine_text import combine_text
from dataclasses import dataclass, field

_ANSI_SUPPORTED = supports_ansi()

@dataclass(slots=True, frozen=True)
class style:
    template: str

    _ansi_supported: bool = field(default=_ANSI_SUPPORTED, init=False, repr=False)

    def __call__(self, *text, force_ansi: bool = False) -> str:
        """ Allows the Style instance to be called like a function to format text. """
        return self.format(combine_text(*text), force_ansi)
    
    def format(self, text: str, force_ansi: bool) -> str:
        """
        Formats the given text with the stored template,
        respecting ANSI support settings.
        """
        if not self._ansi_supported and not force_ansi:
            return text
         
        return self.template.format(text)