import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import strtool.coordinate as coordinate
import strtool.utility as utility


keepends = True
test_str_0 = ""
test_str_1 = "\n"
test_str_2 = "abc\ndef\n\nghi"
test_str_3 = "abc\ndef\n\nghi\n"
test_strings = (test_str_0, \
                test_str_1, \
                test_str_2, \
                test_str_3)

print("test_strings")
for test_str in test_strings:
    utility.print_repr(test_str, keepends)
    print("***")

for test_str in test_strings:
    print(f".get_height(text=...) -> {coordinate.get_height(test_str)}")
    print("***")
print("***")

print(f".get_width(text=..., {keepends=})")
for test_str in test_strings:
    print(coordinate.get_width(test_str, keepends))
print("***")

print(f".get_size(text=..., {keepends=})")
for test_str in test_strings:
    print(coordinate.get_size(test_str, keepends))
print("***")
