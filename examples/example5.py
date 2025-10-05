from rich_style import bold, italic, strikethrough

bold_italic = bold + italic
bold_strikethrough = bold + strikethrough

print(bold_italic("Hello"), bold_strikethrough("World!"))