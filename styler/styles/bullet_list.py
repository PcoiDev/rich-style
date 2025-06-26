from ..core.combine_text import combine_text

_BULLET_TO_TEXT_SPACING = "   "
_BULLETS = ["●", "○", "⦿"]

def bullet_list(*text: str, base_indentation_level: int = 0):
    """Formats a list of text items as a bullet list with customizable indentation."""
    formatted_lines = []

    for item_text in text:
        stripped_text = item_text.lstrip()
        leading_spaces = len(item_text) - len(stripped_text)
        indentation_level = base_indentation_level + (leading_spaces // 4)

        bullet = _BULLETS[indentation_level % len(_BULLETS)]
        indent_str = "  " * indentation_level

        line = combine_text(indent_str, bullet, _BULLET_TO_TEXT_SPACING, stripped_text)
        formatted_lines.append(line)

    return "\n".join(formatted_lines)
