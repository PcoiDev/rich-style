from rich_style import presets, italic, rainbow_text, bold, underline
from rich_style import debug, info, success, timed_print, warn, error

print("--- Styled Text with Colors ---\n")

print(f"This is {italic(presets.red('italic red'))} text.")
print(f"Important: {bold(presets.green('Action required'))} by end of day.")
print(f"Note: {italic(presets.cyan('Optional feature'))} available in settings.")
print(f"Alert: {underline(presets.yellow('Limited time offer'))} expires soon.")

print("\n--- Logging and Messaging ---\n")

debug("Application started successfully.")
debug("Loading configuration from config.json...")

info("Connected to database.")
info("Found 150 records matching your query.")

success("File uploaded successfully!")
success("All tests passed without errors.")

timed_print("Processing your request...")
timed_print("Generating report, please wait...")

warn("Disk space is running low (15% remaining).")
warn("API rate limit: 5 requests remaining this hour.")

error("Failed to connect to remote server.")
error("Invalid credentials provided.")

print("\n--- Rainbow Text Examples ---\n")

print(rainbow_text("Congratulations on your achievement!"))
print(rainbow_text("Welcome to the application!"))
print(f"Status: {rainbow_text('ONLINE')} | Users: 1,234")

print("\n--- Advanced Styled Messages ---\n")

status = "pending"
if status == "approved":
    print(f"Request status: {bold(presets.green(status.upper()))}")
elif status == "rejected":
    print(f"Request status: {bold(presets.red(status.upper()))}")
else:
    print(f"Request status: {italic(presets.yellow(status.upper()))}")

print(f"\nSystem Health:")
print(f"  CPU: {presets.green('Normal')}")
print(f"  Memory: {presets.yellow('Warning - 85% used')}")
print(f"  Disk: {presets.red('Critical - 95% full')}")

print(f"\nUser Dashboard:")
print(f"  Welcome back, {bold(presets.cyan('Alice'))}!")
print(f"  You have {underline(presets.magenta('3 new messages'))}.")
print(f"  Last login: {italic(presets.white('2 hours ago'))}")


print("\n" + "="*50)
print("\n--- Foreground and Background Colors ---\n")

from rich_style import foreground, background

print(foreground(presets.red, "Red text on default background"))
print(foreground(presets.cyan, "Cyan text for information"))
print(foreground(presets.magenta, "Magenta text for highlights"))

print()

print(background(presets.blue, "Text with blue background"))
print(background(presets.green, "Text with green background"))
print(background(presets.yellow, "Text with yellow background"))

print("\n--- Combined Foreground and Background ---\n")

print(foreground(presets.green, background(presets.yellow, "Green text on yellow background")))
print(foreground(presets.white, background(presets.red, "White text on red background - ERROR")))
print(foreground(presets.black, background(presets.cyan, "Black text on cyan background - INFO")))
print(foreground(presets.yellow, background(presets.blue, "Yellow text on blue background")))

print("\n--- Practical Use Cases ---\n")

print(background(presets.red, foreground(presets.white, " CRITICAL ")), "System failure detected")
print(background(presets.yellow, foreground(presets.black, " WARNING ")), "Low memory available")
print(background(presets.green, foreground(presets.white, " SUCCESS ")), "Operation completed")
print(background(presets.blue, foreground(presets.white, "  INFO   ")), "Processing started")

print("\n--- Menu with Colors ---\n")

menu_items = [
    ("1", "View Profile", presets.cyan),
    ("2", "Settings", presets.green),
    ("3", "Help", presets.yellow),
    ("4", "Exit", presets.red)
]

for num, label, color in menu_items:
    print(f"  [{bold(color(num))}] {foreground(color, label)}")


print("\n" + "="*50)
print("\n--- Style Combinations ---\n")

from rich_style import strikethrough

bold_italic = bold + italic
bold_strikethrough = bold + strikethrough
italic_underline = italic + underline
all_styles = bold + italic + underline

print(bold_italic("Hello"), bold_strikethrough("World!"))
print(f"This is {bold_italic('emphasized text')} in a sentence.")
print(f"Old price: {bold_strikethrough('$99.99')} New price: {bold(presets.green('$79.99'))}")

print()

print(f"Features: {italic_underline('Advanced search')}, {italic_underline('Auto-save')}, {italic_underline('Dark mode')}")
print(f"Status: {all_styles('IMPORTANT ANNOUNCEMENT')}")

print("\n--- Style Combinations in Context ---\n")

todo_items = [
    ("Buy groceries", False),
    ("Finish report", True),
    ("Call dentist", False),
    ("Submit timesheet", True)
]

print(bold("To-Do List:\n"))
for task, completed in todo_items:
    if completed:
        print(f"  ✓ {bold_strikethrough(task)}")
    else:
        print(f"  ○ {task}")

print(f"\nDocument Status:")
print(f"  Draft: {italic('In progress')}")
print(f"  Review: {bold_italic('Pending approval')}")
print(f"  Published: {bold(presets.green('Live'))}")

print("\n--- Complex Combinations ---\n")

header_style = bold + underline
highlight_style = bold + italic
deprecated_style = strikethrough + italic

print(header_style("Project Overview"))
print(f"\nThe {highlight_style('new feature')} is now available.")
print(f"The {deprecated_style('old API endpoint')} will be removed soon.")
print(f"Please use {bold(presets.blue('version 2.0'))} going forward.")