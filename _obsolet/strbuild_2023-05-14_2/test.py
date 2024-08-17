from strclass import *




class Test:

    def __init__(self):

        self.attr_int = 0
        self.attr_float = 0.0
        self.attr_str = "string"
        self.attr_list = ["a", "b", "c"]
        self.attr_tuple = ("a", "b", "c")
        self.attr_set = {"a", "b", "c"}
        self.attr_dict = {0: "a", 1: "b", 2: "c"}
        self.attr_dict2 = {"0": "a", "1": "b", "2": "c"}


test0 = Test()

print(test0)

print(str_class_attrs(test0))


