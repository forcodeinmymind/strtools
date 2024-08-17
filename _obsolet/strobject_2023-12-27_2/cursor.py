"""
Module for text cursor functions to move a cursor inside given text space

Functions
---------
increment_column
    increment cursor position x on line

increment_horizontal
    ?

increment_line
    ?

increment_vertical
    ?

test_cursorfunction
    Check if the functions above work as intended
"""

keeplinebreaks = True


def increment_column(text: str = str(), \
                     pos: tuple[int, int] = (0, 0), \
                     keeplinebreaks: bool = True, \
                     ascend: bool = True) \
                     -> tuple[int, int]:
    """
    Increment parameter (cursor)'pos' (x, y)
    ascending or descending depending parameter 'ascend'.
    Parameter 'ascend'=True:
        if x + 1 < len(line): x+=0
        elif line + 1 < len(text.splitlines()): x=0, y+=1
        else: x=0, y=0
    """
    X = 0
    Y = 1
    LEN_LINES = tuple(len(str_line) for str_line in text.splitlines(keeplinebreaks))

    if ascend:
        if pos[X] < (LEN_LINES[pos[Y]] - 1):
            return (pos[X] + 1), pos[Y]
        elif pos[Y] < (len(LEN_LINES) - 1):
            return 0, (pos[Y] + 1)
        else:
            return 0, 0
    else:
        if pos[X] > 0:
            return (pos[X] - 1), pos[Y]
        elif pos[Y] > 0:
            return LEN_LINES[pos[Y] - 1] - 1, (pos[Y] - 1)
        else:
            return LEN_LINES[len(LEN_LINES) - 1] - 1, len(LEN_LINES) - 1

def increment_horizontal(text: str = str(), \
                         pos: tuple[int, int] = (0, 0), \
                         keeplinebreaks: bool = True, \
                         ascend: bool = True) \
                         -> tuple[int, int]:
    """
    ?
    """
    X = 0
    Y = 1
    LEN_LINES = tuple(len(str_line) for str_line in text.splitlines(keeplinebreaks))

    if ascend:
        if pos[X] < (LEN_LINES[pos[Y]]):
            return (pos[X] + 1), pos[Y]
        elif pos[Y] < (len(LEN_LINES) - 1):
            return 0, (pos[Y] + 1)
        else:
            return 0, 0
    else:
        if pos[X] > 0:
            return (pos[X] - 1), pos[Y]
        elif pos[Y] > 0:
            return LEN_LINES[pos[Y] - 1], (pos[Y] - 1)
        else:
            return LEN_LINES[len(LEN_LINES) - 1], len(LEN_LINES) - 1

def increment_line(text: str = str(), \
                   pos: tuple[int, int] = (0, 0), \
                   keeplinebreaks: bool = True, \
                   ascend: bool = True) \
                   -> tuple[int, int]:
    """
    ?
    """
    X = 0
    Y = 1
    LEN_LINES = tuple(len(str_line) for str_line in text.splitlines(keeplinebreaks))

    if ascend:
        if pos[Y] > 0:
            if pos[X] < LEN_LINES[pos[Y] - 1]:
                return pos[X], pos[Y] - 1
            else:
                return LEN_LINES[pos[Y] - 1] - 1, pos[Y] - 1
        else:
            if pos[X] < LEN_LINES[len(LEN_LINES) - 1]:
                return pos[X], len(LEN_LINES) - 1
            else:
                return LEN_LINES[len(LEN_LINES) - 1] - 1, len(LEN_LINES) - 1
    else:
        if pos[Y] < len(LEN_LINES) - 1:
            if pos[X] < LEN_LINES[pos[Y] + 1]:
                return pos[X], pos[Y] + 1
            else:
                return LEN_LINES[pos[Y] + 1] - 1, pos[Y] + 1
        else:
            if pos[X] < LEN_LINES[0]:
                return pos[X], 0
            else:
                return LEN_LINES[0] - 1, 0

def increment_vertical(text: str = str(), \
                       pos: tuple[int, int] = (0, 0), \
                       keeplinebreaks: bool = True, \
                       ascend: bool = True) \
                       -> tuple[int, int]:
    """
    ?
    """
    X = 0
    Y = 1
    LEN_LINES = tuple(len(str_line) for str_line in text.splitlines(keeplinebreaks))

    if ascend:
        if pos[Y] > 0:
            if pos[X] <= LEN_LINES[pos[Y] - 1]:
                return pos[X], pos[Y] - 1
            else:
                return LEN_LINES[pos[Y] - 1], pos[Y] - 1
        else:
            if pos[X] <= LEN_LINES[len(LEN_LINES) - 1]:
                return pos[X], len(LEN_LINES) - 1
            else:
                return LEN_LINES[len(LEN_LINES) - 1], len(LEN_LINES) - 1
    else:
        if pos[Y] < len(LEN_LINES) - 1:
            if pos[X] <= LEN_LINES[pos[Y] + 1]:
                return pos[X], pos[Y] + 1
            else:
                return LEN_LINES[pos[Y] + 1], pos[Y] + 1
        else:
            if pos[X] <= LEN_LINES[0]:
                return pos[X], 0
            else:
                return LEN_LINES[0], 0


def test_cursorfunction(function=None, text=str(), pos=(0, 0), keeplinebreaks=True, ascend=True):
    str_func = str(function)[str(function).find(" ") + 1:]
    str_func = str_func[:str_func.find(" ")]
    print(f".test_cursorfunction({str_func}, {text:.6}..., {pos}, {keeplinebreaks}, {ascend})")
    for i, char in enumerate(text):
        if char == "\n":
            char = " "
        len_line = len(text.splitlines(keeplinebreaks)[pos[1]])
        print(f"[{i:3}, {char}] .{str_func}() -> ({pos[0]:2}, {pos[1]:2}), len()={len_line}")
        pos = function(text, pos, keeplinebreaks, ascend)


if __name__ == "__main__":
    str_test_3 = "abcdefghij\nklmnopqrst\nuvwxyzABCD\nEFGHIJKLMN"
    print(str_test_3)
    pos = (0, 0)
    test_cursorfunction(increment_column, str_test_3, pos, keeplinebreaks, True)
