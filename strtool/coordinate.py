"""module for text coordinates and indices
`text array`, `text grid`
len("".splitlines()) == 0
len("abc".splitlines()) == 1
len("abc\n".splitlines()) == 2
"""


def get_height(text: str) -> int:
    """length of text lines as int
    `\n` is two lines
    `` is one line
    """
    if not len(text):
        return 1
    elif text.endswith("\n"):
        return len(text.splitlines()) + 1
    else:
        return len(text.splitlines())

def get_width(text: str, keepends: bool = False) -> int:
    max_width = 0
    for line in text.splitlines(keepends):
        if len(line) > max_width:
            max_width = len(line)
    return max_width

def get_size(text: str, keepends: bool = False) -> tuple[int, int]:
    if not len(text):
        return (0, 1)
    else:
        max_width = 0
        for index, line in enumerate(text.splitlines(keepends)):
            if len(line) > max_width:
                max_width = len(line)
        if text.endswith("\n"):
            index += 2
        else:
            index += 1
        return max_width, index

def text_pos_to_index(text: str, pos: tuple[int, int], keepends: bool = False) -> int:
    return sum(len(str_line) for str_line in text.splitlines()[0:pos[1]]) + pos[0]

