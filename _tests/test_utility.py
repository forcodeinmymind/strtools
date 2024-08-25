import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import strtool.utility as utility


test_str = "abc\ndef\nghi"
test_str_2 = "abc\ndef\nghi\n"


utility.print_repr(test_str_2)
print("***")
utility.print_repr(test_str_2, True)
