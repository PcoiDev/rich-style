def combine_text(*text: str, separator: str = "") -> str:
    return separator.join(str(t) for t in text)