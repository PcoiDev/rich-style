# rich-style

A Python library for creating and applying full-color, linear, and circular gradients to text with easy color management. Includes utilities for ANSI styling, colored prints, and more.

## Features

- **Text Styling:** Bold, italic, underline, strikethrough, bullet lists, and more.
- **Color Management:** Use named presets, custom RGB, gradients, and HSL/HTML color parsing.
- **Gradients:** Linear and circular gradients for text.
- **ANSI Support:** Automatically detects terminal support for ANSI escape codes.
- **Utility Prints:** Info, warning, error, success, timed, and mutable prints with color.
- **Composable:** Combine styles and colors easily.

## Installation

```sh
pip install rich-style
```

## Usage

Basic Styling

```py
from rich_style import bold, italic, underline, strikethrough

print(bold("Bold text"))
print(italic("Italic text"))
print(underline("Underlined text"))
print(strikethrough("Strikethrough text"))
```

Bullet Lists

```py
from rich_style import bullet_list, bold

tasks = [
    "Complete report",
    "Send email to client",
    "Buy groceries"
]

print(bold("Task List:"))
print(bullet_list(*tasks))
```

Colors and Gradients

```py
from rich_style import presets, foreground, background

print(foreground(presets.red, "Red text"))
print(background(presets.blue, "Text with blue background"))
```

Colors and Gradients

```py
from rich_style import presets, foreground, background

print(foreground(presets.red, "Red text"))
print(background(presets.blue, "Text with blue background"))
```

Rainbow Text

```py
from rich_style import rainbow_text
print(rainbow_text("This is a rainbow text message."))
```

Utility Prints

```py
from rich_style import info, success, warn, error, timed_print

info("This is an informational message.")
success("This is a success message.")
warn("This is a warning message.")
error("This is an error message.")
timed_print("This is a timed print message.")
```

Mutable Print
```py
from rich_style import mutable_print
from time import sleep

mutable = mutable_print("Loading")
sleep(1)
mutable("Still loading...")
sleep(1)
mutable("Done!\n")
```

> [!WARNING]  
> You can only use a mutable print when it's the last print.

## Examples

See the `examples/` directory for more usage examples.

## Credits

- **Author:** [PcoiDev](https://github.com/PcoiDev)
- **Inspiration:** [colorama](https://github.com/tartley/colorama), [rich](https://github.com/Textualize/rich) and [stylepy](https://github.com/web-slate/stylepy).

## License

This project is licensed under the `MIT License`.