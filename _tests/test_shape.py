"""test strtool.shape
1.0.0
2024-08-17
"""

import os
import sys
import string

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import strtool.shape as shape
import strtool.utility as utility

# string.printable
"""
with open("test_textblock2.txt", "r", encoding='utf8') as file:
    str_test = file.read()
str_test = string.printable
"""

str_test = """0123456789abcdef
ghijklmnopqrstuv
wxyzABCDEFGHIJKL
MNOPQRSTUVWXYZ!"
#$%&'()*+,-./:;<
=>?@[\]^_`{|}~"""

print("\nstr_test\n", str_test)
max_len = 6
print(f"\nshape.newline_at(string=..., {max_len=})\n", shape.newline_at(str_test, max_len))
print("\nshape.add_line_numbers\n", utility.add_line_numbers(shape.newline_at(str_test, max_len)), "\n")

str_test = shape.newline_at(str_test, 16)
print("\nstr_test\n")
utility.print_repr(str_test)
print("\n")
start = 2
end = 4
print(f"shape.slice_lines(string=..., {start=:}, {end=:})")
utility.print_repr(shape.slice_lines(str_test, start, end))

print("\n")
str_test = "abc\ndef\nghi"
# str_test = "abc\ndef\nghi\n"
utility.print_repr(str_test)
length = 5
print(f"\nshape.pad_bottom(string=..., {length=})")
utility.print_repr(shape.pad_bottom(str_test, length))
print(f"\nshape.pad_top(string=..., {length=})")
utility.print_repr(shape.pad_top(str_test, length))

# .endswith("\n")
print("\n")
str_test = "abc\ndef\nghi\n"
print("".join(repr(line).replace("'", "") for line in shape.splitlines(str_test, True)))
# utility.print_repr("".join(shape.splitlines(str_test, True)), True)
