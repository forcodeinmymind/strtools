


def add_line_numbers(text: str, keepends: bool = False) -> str:
    max_linenumb = len(str(len(text.splitlines(keepends))))
    return "\n".join(f"[{i:0{max_linenumb}}]{str_line}" for i, str_line in enumerate(text.splitlines(keepends)))

def print_repr(text: str, keepends: bool = False) -> None:
    if len(text.splitlines(keepends)):
        for str_line in text.splitlines(keepends):
            print(repr(str_line))
        # if text.endswith("\n"):
        #     print(repr(""))
    else:
        print(repr(""))
