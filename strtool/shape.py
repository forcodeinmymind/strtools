"""module for shaping str
1.0.0
2024-08-17

len(.splitlines())
len("...\n".splitlines()) == 1
len("...".splitlines()) == 1
len("".splitlines()) == 0
slice
[start:stop:step] stop == len(sequence) | None
"""

def newline_at(string: str, max_len: int) -> str:
    """wrapping str max line len with `\n`"""
    new_string = str()
    for str_line in string.splitlines():
        if len(str_line) > max_len:
            new_string += "\n".join(str_line[i:i + max_len] for i in range(0, len(str_line), max_len)) + "\n"
        else:
            new_string += str_line + "\n"
    return new_string

def slice_lines(string: str, start: int, end: int | None = None) -> str:
    """if end >= len(string): end = len(string); No IndexError"""
    return "\n".join(str_line for str_line in string.splitlines()[start:end])

def slice_lines_last(string: str, length: int) -> int:
    return len(string.splitlines()) - length

def pad_bottom(string: str, length: int) -> str:
    if not string.endswith(("\n", "\r\n", "\r")):
        string += "\n"
    return string + "\n" * (length - len(string.splitlines()))

def pad_top(string: str, length: int) -> str:
    len_lines = length - len(string.splitlines())
    return "\n" * len_lines + string
