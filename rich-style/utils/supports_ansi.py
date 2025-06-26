from sys import platform, stdout
from functools import lru_cache
from os import environ

@lru_cache(maxsize=None)
def supports_ansi() -> bool:
    """Detects if the current terminal likely supports ANSI escape codes."""

    if environ.get('NO_COLOR'):
        return False
    if environ.get('CLICOLOR_FORCE'):
        return True

    is_tty = hasattr(stdout, 'isatty') and stdout.isatty()

    if not is_tty:
        return False

    if platform == 'win32':
        if environ.get('ANSICON') is not None or environ.get('TERM_PROGRAM') == 'vscode' or 'CONEMUANSI' in environ:
            return True
        try:
            from ctypes import windll, c_ulong, byref

            k32 = windll.kernel32
            h_out = k32.GetStdHandle(-11)
            mode = c_ulong()

            k32.GetConsoleMode(h_out, byref(mode))
            if (mode.value & 0x0004) == 0:
                k32.SetConsoleMode(h_out, mode.value | 0x0004)

            return True
        except Exception:
            pass
    else:
        term = environ.get('TERM', '').lower()
        if 'xterm' in term or 'color' in term or 'screen' in term or 'tmux' in term:
            return True

    return False