from sys import stdout

def mutable_print(text: str):
    """Prints a message that can be updated in place."""
    
    stdout.write(text)
    stdout.flush()

    def update(new_text: str):
        """Updates the printed message with new text."""

        stdout.write('\r\033[K' + new_text)
        stdout.flush()

    return update
