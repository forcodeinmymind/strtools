"""
Test Environment for strobject
"""



"""
import sys
import os
sys.path.append(os.path.join("E:/Programmieren/Python/Module"))
import logger
"""

import strobject

import pygame



dict_test_0 = {"a": 123, 2: "abc", None: None}
dict_test_1 = {"a": 123, 2: "abc", None: None, "list0": [0, 1, 2]}
nested_dict = {"a": {"a0": {"a00", "b00", "c00"}, "b0": {"e00", "f00", "g00"}, "c0": {"h00", "i00", "j00"}}, "b": {"a1": 0, "b1": 1, "c1": 2}, "c": {"a2": 0, "b2": 1, "c2": 2}}
nest2_dict = {"a": {"a": {"a": 0, "b": 1, "c": 2}, "b": {"a": 0, "b": 1, "c": 2}, "c": {"a": 0, "b": 1, "c": 2}}, "b": {"a": {"a": 0, "b": 1, "c": 2}, "b": {"a": 0, "b": 1, "c": 2}, "c": {"a": 0, "b": 1, "c": 2}}, "c": {"a": {"a": 0, "b": 1, "c": 2}, "b": {"a": 0, "b": 1, "c": 2}, "c": {"a": 0, "b": 1, "c": 2}}}

set_test = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"}
tuple_test = ("a", "b", "c")
nested_tuple = ((0, 1, 2), ("a", "b", "c"))
nest3_tuple = (((0, 1, 2), ), )
nest4_tuple = ((((0, 1, 2), (0, 1, 2))))

# nested_set = {{0, 1}, {2, 3}} -> TypeError: unhashable type: 'set'
# nested_set = {["ns_l1_0", "ns_l1_1", "ns_l1_3"], ["ns_l2_0", "ns_l2_1", "ns_l2_3"]} -> TypeError: unhashable type: 'set'


class Test:

    def __init__(self):

        self.integer = 123
        self.float = 0.123
        self.string = "string"

        self.set0 = set_test
        self.tuple0 = tuple_test
        self.dict0 = nest2_dict

    def classmethod0(self):

        print("call classmethod0")



class TestChild(Test):

    def __init__(self):

        super().__init__()



test0 = Test()
testchild0 = TestChild()

rect0 = pygame.Rect(0, 0, 64, 64)


# print(strobject.strnested(rect0))

# print(strobject.strnested(testchild0))

print(strobject.str_object([testchild0, testchild0, testchild0], False, True, None))
