from sys import stdout
_last_was_mutable = False

def mutable_print(text: str):
    global _last_was_mutable

    stdout.write(text)
    stdout.flush()
    _last_was_mutable = True

    def update(new_text: str, finalize: bool = False):
        global _last_was_mutable

        stdout.write('\r\033[K' + new_text)
        if finalize:
            stdout.write('\n')
            _last_was_mutable = False
        stdout.flush()

    return update
