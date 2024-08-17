


keeplinebreaks = True


def pos_to_index(string: str, pos:tuple[int, int]) -> int:
    """
    Returns the index of parameter 'pos'
    :param string: Any str()
    :type string: str
    :param pos:
    :type pos: int
    """
    return sum(len(str_line) for str_line in string.splitlines(keeplinebreaks)[0:pos[1]]) + pos[0]


def increment_column(text: str = str(), \
                     pos: tuple[int, int] = (0, 0), \
                     keeplinebreaks: bool = True, \
                     ascend: bool = True) \
                     -> tuple[int, int]:

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


def increment_cursor_horizontal(text: str = str(), \
                                pos: tuple[int, int] = (0, 0), \
                                keeplinebreaks: bool = True, \
                                ascend: bool = True) \
                                -> tuple[int, int]:

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


def increment_cursor_vertical(text: str = str(), \
                              pos: tuple[int, int] = (0, 0), \
                              keeplinebreaks: bool = True, \
                              ascend: bool = True) \
                              -> tuple[int, int]:

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



if __name__ == "__main__":

    with open("test_textblock.txt", "r", encoding='utf8') as file:
        str_textblock = file.read()

    str_test = "012\n345\n678"
    str_test_2 = "abcde\nfghij\nklmno\npqrst"
    str_test_3 = "abcdefghij\nklmnopqrst\nuvwxyzABCD\nEFGHIJKLMN"

    print(str_test_3)
    print(pos_to_index((2, 2), str_test_3))

