"""module for shaping str
1.0.0
2024-08-17

Notes
-----
len(.splitlines())
len("...\n".splitlines()) == 1
len("...".splitlines()) == 1
len("".splitlines()) == 0
slice
[start:stop:step] stop == len(sequence) | None
text.splitlines()[-length:None]
"""

def splitlines(text: str, keepends: bool = False) -> list[str]:
    if len(text):
        lines = text.splitlines(keepends)
        if text.endswith("\n"):
            lines.append("")
        return lines
    else:
        return ["", ]

def slice_lines(text: str, start: int = 0, end: int | None = None) -> str:
    """if end >= len(text): end = len(text); No IndexError"""
    return "\n".join(str_line for str_line in splitlines(text)[start:end])

def newline_at(text: str, max_len: int) -> str:
    new_text = str()
    for line in splitlines(text, True):
        new_text += "\n".join([line[i:i+max_len] for i in range(0, len(line), max_len)])
    return new_text

def pad_bottom(text: str, length: int, keepends: bool = False) -> str:
    if not text.endswith(("\n", "\r\n", "\r")):
        text += "\n"
    return text + "\n" * (length - len(splitlines(text, keepends)))

def pad_top(text: str, length: int, keepends: bool = False) -> str:
    len_lines = length - len(splitlines(text, keepends))
    return "\n" * len_lines + text
