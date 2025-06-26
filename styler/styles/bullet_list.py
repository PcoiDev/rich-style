from ..core.combine_text import combine_text

BULLET_TO_TEXT_SPACING = "   "
BULLETS = ["●", "○", "⦿"]

def bullet_list(*text: str, base_indentation_level: int = 0):
    formatted_lines = []

    for item_text in text:
        stripped_text = item_text.lstrip()
        leading_spaces = len(item_text) - len(stripped_text)
        indentation_level = base_indentation_level + (leading_spaces // 4)

        bullet = BULLETS[indentation_level % len(BULLETS)]
        indent_str = "  " * indentation_level

        line = combine_text(indent_str, bullet, BULLET_TO_TEXT_SPACING, stripped_text)
        formatted_lines.append(line)

    return "\n".join(formatted_lines)
