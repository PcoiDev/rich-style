from rich_style import bold, italic, underline, strikethrough, bullet_list

print("--- Text Styling Examples ---")

# Basic usage
print(f"This is {bold('important')} information.")
print(f"This is a {italic('sidebar comment')}.")
print(f"Please {underline('pay attention')} to this line.")
print(f"This item is {strikethrough('no longer available')} in stock.")

print("\n--- Combining Styles ---")

bold_italic = bold + italic
italic_underline = italic + underline
bold_strikethrough = bold + strikethrough
underline_bold_italic = underline + bold + italic

print(f"This text is {bold_italic('bold and italic')}.")
print(f"This text is {italic_underline('italic and underlined')}.")
print(f"This text is {bold_strikethrough('bold and struck through')}.")
print(f"This text is {underline_bold_italic('all three basic styles')}.")

print("\n--- Styling within Sentences ---")

message = f"Thank you for your {bold('support')}. Your {italic('feedback')} is greatly {underline('appreciated')}."
print(message)

item_status = "Available"
if item_status == "Available":
    print(f"Status: {bold(item_status)}")
else:
    print(f"Status: {strikethrough(item_status)}")

print("\n--- Styling a List ---")

# Default indentation (level 0)
tasks = [
    "Complete report",
    "Send email to client",
    "Buy groceries"
]
print(bold("Task List (Default Indent):"))
print(bullet_list(*tasks))

# With custom indentation level
chores = [
    "Take out trash",
    "Wash dishes",
    "Feed pet"
]
print(bold("\nDaily Chores (Indented Level 1):"))
print(bullet_list(*chores, base_indentation_level=1))

# Combining styling with list formatting
notes = [
    f"{bold("Review meeting agenda")}",
    f"    {italic("Draft project proposal")}",
    f"        {underline("Submit expense report")}",
    f"            {strikethrough("Old item (done)")}"
]

print(bold("\nImportant Notes:"))
print(bullet_list(*notes))

# Nested list with dynamic indentation from leading spaces
print(bold("\nNested List Example (Illustrative):"))
print(bullet_list(
    "Item 1",
    "    Subitem 1.1",
    "    Subitem 1.2",
    "Item 2",
    "    Subitem 2.1",
    "        Sub-subitem 2.1.1"
))