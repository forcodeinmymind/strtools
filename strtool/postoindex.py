


keeplinebreaks = True


def pos_to_index(text: str, pos:tuple[int, int]) -> int:
    """
    Returns the index of parameter 'pos' inside 'text'
    Parameter 'pos' values >= text length may produce false results!
    
    :param string: Any str()
    :type string: str
    :param pos:
    :type pos: int
    :returns: int; index of 'pos'
    """
    return sum(len(str_line) for str_line in text.splitlines(keeplinebreaks)[0:pos[1]]) + pos[0]

def test(text=str()):
    """
    Function for testing '.pos_to_index()'
    """
    print("test: .pos_to_index()")
    for row, strline in enumerate(text.splitlines(keeplinebreaks)):
        for column, char in enumerate(strline):
            if char == "\n":
                char = " "
            print(f"[{column:2}, {row:2}, {char}] .pos_to_index({column:2}, {row:2}) -> {pos_to_index(text, (column, row)):2}")

if __name__ == "__main__":

    with open("test_textblock.txt", "r", encoding='utf8') as file:
        str_textblock = file.read()

    str_test = "abcdefghij\nklmnopqrst\nuvwxyzABCD\nEFGHIJKLMN"

    print(str_test + "\n")
    test(str_test)
    pos = (100, 100)
    print(f"{pos=} -> {pos_to_index(str_test, pos)}")
