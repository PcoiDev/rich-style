from styler import presets, italic, info, success, timed_print, warn, error, rainbow_text

print(f"a {italic(presets.red("italic red"))} text")

info("This is an informational message.")
success("This is a success message.")
timed_print("This is a timed print message.")
warn("This is a warning message.")
error("This is an error message.")

print(rainbow_text("This is a rainbow text message."))