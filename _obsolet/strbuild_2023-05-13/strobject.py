

__fillchar = "_"



def strlevelpadding(level=int(), fillchar=None):

    if fillchar == None:

        fillchar = __fillchar

    return level * fillchar


def stripfirstnewline(string=str()):

    if string[0] == "\n":

        return string[1: ]

    else:

        return string


def strobject(obj=None, level=int(), fillchar=None):

    if fillchar == None:

        fillchar = __fillchar


    if type(obj) == str:

        return obj

    elif type(obj) in (int, float) or obj ==None:

        string = str(obj)

    elif type(obj) in (set, tuple, list):

        string = strsequence(obj, level)

    elif type(obj) is dict:

        string = strdict(obj, level)

    else:

        string = strclass(obj, level, fillchar)

        # raise TypeError("strobject(obj={0}, level={1}, fillchar={2})\nUnknown tpye({0}): {3}".format(obj, level, fillchar, type(obj)))

    return string


def strsequence(obj_set=None, level=int(), fillchar=None):

    string = str()

    for i, e in enumerate(obj_set):

        string = string + "\n"

        string = string + strlevelpadding(level, fillchar) + "[{}]".format(str(i).rjust(len(str(len(obj_set) - 1)), "0"))

        str_value = strobject(e, level + 1, fillchar)

        if "\n" not in str_value:

            string = string + " "

        string = string + str_value

    return string


def strdict(obj_dict=None, level=int(), fillchar=None):

    try:
        maxlen = max(len(str(key)) for key in obj_dict.keys())
        
    except ValueError:
        
        maxlen = int()
        
    space = 1
    string = str()

    for key in obj_dict.keys():

        string = string + "\n"

        string = string + strlevelpadding(level, fillchar) + str(key).ljust(((maxlen - 1) + space), " ")

        str_value = strobject(obj_dict[key], level + 1, fillchar)

        if "\n" not in str_value:

            string = string + " "

        string = string + str_value

    return string


def strclass(obj_class=None, level=int(), fillchar=None):

    class_dict = dict(zip(obj_class.__dict__.keys(), [getattr(obj_class, key) for key in obj_class.__dict__.keys()]))

    string = str(obj_class) + strobject(class_dict, level + 1, fillchar)

    return string





if __name__ == "__main__":

    dict_test_0 = {"a": 123, 2: "abc", None: None}
    dict_test_1 = {"a": 123, 2: "abc", None: None, "list0": [0, 1, 2]}
    nested_dict = {"a": {"a0": {"a00", "b00", "c00"}, "b0": {"e00", "f00", "g00"}, "c0": {"h00", "i00", "j00"}}, "b": {"a1": 0, "b1": 1, "c1": 2}, "c": {"a2": 0, "b2": 1, "c2": 2}}
    nest2_dict = {"a": {"a": {"a": 0, "b": 1, "c": 2}, "b": {"a": 0, "b": 1, "c": 2}, "c": {"a": 0, "b": 1, "c": 2}}, "b": {"a": {"a": 0, "b": 1, "c": 2}, "b": {"a": 0, "b": 1, "c": 2}, "c": {"a": 0, "b": 1, "c": 2}}, "c": {"a": {"a": 0, "b": 1, "c": 2}, "b": {"a": 0, "b": 1, "c": 2}, "c": {"a": 0, "b": 1, "c": 2}}}

    set_test = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"}
    tuple_test = ("a", "b", "c")
    nested_tuple = ((0, 1, 2), ("a", "b", "c"))
    nest3_tuple = (((0, 1, 2), ), )
    nest4_tuple = ((((0, 1, 2), (0, 1, 2), (0, 1, 2)), ((0, 1, 2), (0, 1, 2), (0, 1, 2)), ((0, 1, 2), (0, 1, 2), (0, 1, 2))), (((0, 1, 2), (0, 1, 2), (0, 1, 2)), ((0, 1, 2), (0, 1, 2), (0, 1, 2)), ((0, 1, 2), (0, 1, 2), (0, 1, 2))), (((0, 1, 2), (0, 1, 2), (0, 1, 2)), ((0, 1, 2), (0, 1, 2), (0, 1, 2)), ((0, 1, 2), (0, 1, 2), (0, 1, 2))))
    

    class Test:

        def __init__(self):

            self.integer = 123
            self.float = 0.123
            self.string = "string"

            self.tuple0 = tuple_test
            self.dict0 = nest2_dict

        def classmethod0(self):

            print("call classmethod0")

    test_class = Test()

    # print(strdict(dict_test_1))

    # print(strobject(dict_test_0))

    # print(strobject(set_test))

    # print(strset(set_test, int(), " "))

    # print(strdict(dict_test_0))

    # print(strobject(tuple_test))
    # print(strobject(nested_tuple))
    # print(strobject(dict_test_1))
    # print(strobject(nest3_tuple))
    # print(strobject(nest4_tuple))

    # print(strobject(nested_dict))
    # print(strobject(nest2_dict))
    
    print(strclass(test_class))
