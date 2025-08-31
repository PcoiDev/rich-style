from rich_style import presets, foreground, background

print(foreground(presets.red, "Red text"))
print(background(presets.blue, "Text with blue background"))

print(foreground(presets.green, background(presets.yellow, "Green text with yellow background")))