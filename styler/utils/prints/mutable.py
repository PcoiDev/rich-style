from sys import stdout
_last_was_mutable = False

def mutable_print(text: str):
    """Prints a message that can be updated in place."""
    global _last_was_mutable

    stdout.write(text)
    stdout.flush()
    _last_was_mutable = True

    def update(new_text: str, finalize: bool = False):
        """Updates the printed message with new text."""
        global _last_was_mutable

        stdout.write('\r\033[K' + new_text)
        if finalize:
            stdout.write('\n')
            _last_was_mutable = False
        stdout.flush()

    return update
