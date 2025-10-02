from enum import Enum, auto

class gradient_type(Enum):
    LINEAR = auto(),
    CIRCULAR = auto(),
    
class layers(Enum):
    BACKGROUND = auto(),
    TEXT = auto(),
    FULL = auto()
    