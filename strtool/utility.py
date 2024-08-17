

def add_line_numbers(string: str) -> str:
    max_linenumb = len(str(len(string.splitlines())))
    return "\n".join(f"[{i:{max_linenumb}}]{str_line}" for i, str_line in enumerate(string.splitlines()))

def print_repr(string: str) -> None:
    for str_line in string.splitlines(True):
        print(repr(str_line))