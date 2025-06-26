def combine_text(*text: str, separator: str = "") -> str:
    """Combines multiple text strings into one, separated by the specified separator. """
    return separator.join(str(t) for t in text)