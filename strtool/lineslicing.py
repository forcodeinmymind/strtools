"""
?
"""

# last = len()

# Python slicing:
# sequence[start:end]
# if end = None, end = len(sequence); sequence[int():None] -> full sequence


def len_lines(text=str()):

    return text.count("\n")


def clip_lines(text=str(), start=int(), end=None, keepends=False):
    """
    Unnecessary!
    """
    # end = len(text)
    # end > len(text) -> list[start:len(text)]
    # end < start     -> slice off from end [start:len(text) - x]

    # text_clip = "\n".join(text.splitlines()[start:end])
    # -> string with lines from start to end

    return text.splitlines(keepends)[start:end]

def str_lines(text=str(), start=int(), end=None, keepends=False):
    """
    Unnecessary!
    """
    return "\n".join(text.splitlines(keepends)[start:end])

def get_start(len_text=int(), len_clip=int(), end=None, alignment=int()):
    """
    ?
    """
    # max_end = len_text
    # 'start' can be negative; if not use max(0, end - len_clip)

    DEFAULT_ALIGN_TOP = 0
    DEFAULT_ALIGN_BOTTOM = 1

    if end == None:
        if alignment == DEFAULT_ALIGN_TOP:
            end = len_clip
        else:
            end = len_text
    start = max(int(), end - len_clip)
    return start

def get_end(len_text=int(), len_clip=int(), start=int()):
    """
    ?
    """

    return min(start + len_clip, len_text)

def ratio_start(len_text=int(), len_area=int(), ratio=float()):
    """
    ?
    """
    if ratio < 0.0 or ratio > 1.0:
        raise ValueError()
    elif len_area > len_text:
        raise IndexError()
    else:
        return int((ratio * (len_text - len_area)) + 0.5)


def line_padding(len_text=int(), len_area=int()):
    """
    ?
    """
    # len_area > len_text
    # if alignment == end: add empty lines in front
    # else: add empty lines at the back

    pass


def scroll_down(len_text=int(), len_area=int(), start=int(), increment=int()):
    """
    ?
    """
    pass



#



# ...

str_test = """0 das ist der test
1 string, er ist super.
2 ich hatte noch nie
3 so einen tollen test-string
4 hoffenltich macht es das
5 leichter, coole neue
6 programme zu schreiben.
7 wie immer bin ich
8 sehr motiviert und versuche
9 das ganze extrem geil
10 zu lösen und dafür
11 meinen ganzen verstand
12 ein zu setzen,
13 auf gehts!
"""

str_test2 = """0 das ist der test
1 string, er ist super.
2 ich hatte noch nie
3 so einen tollen test-string
4 hoffenltich macht es das
5 leichter, coole neue
6 programme zu schreiben.
7 wie immer bin ich
8 sehr motiviert und versuche
"""
