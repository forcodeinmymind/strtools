

__fillchar = "_"
__strtype = False
__strnamespace = False
__strnested = True



def set_strtype(state=True):

    global __strtype

    __strtype = state


def get_strtype():

    return __strtype


def set_fillchar(fillchar="_"):

    global __fillchar

    __fillchar = fillchar="_"


def set_strnested(state=True):

    global __strnested

    __strnested = state




def strlevelpadding(level=int()):

    return level * __fillchar


def strtype(obj=None):

    str_type = str(type(obj))

    return str_type[str_type.find("'") + 1:-2]


def strobject(obj=None, level=int()):

    if type(obj) in (bool, int, float, str) or \
       obj == None:

        return strvalue(obj, level)

    elif type(obj) in (set, tuple, list):

        return strsequence(obj, level)

    elif type(obj) is dict:

        return strdict(obj, level)

    else:

        return strclass(obj, level)


def strvalue(value=None, level=int(), fillchar=None):

    if __strtype:

        return "{}[{}]{}".format(strlevelpadding(level), str(type(value)), str(value))

    else:

        return "{}{}".format(strlevelpadding(level), str(value))


def strsequence(sequence=None, level=int()):

    string = str()

    for count, item in enumerate(sequence):

        string = string.join([strany(item, level + 1), "\n"])

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

    if not hasattr(obj_class, "__dict__"):

        # return "strobject(obj={}, level={}, fillchar={})\nexcept not hasattr dict".format(obj_class, level, fillchar)

        return str(obj)

    else:
        
        """
        RecursionError possible!
        
        class_dict = dict(zip(obj_class.__dict__.keys(), \
                              [getattr(obj_class, key) for key in obj_class.__dict__.keys()]))

        return str(obj_class) + strobject(class_dict, level + 1, fillchar)
        """

        pass


# sequence is a data type that has ordered items


def strnested(obj=None):

    object_stack = [obj, ]
    indices = list()
    classes = set()
    cur_container_type = str()
    cur_container_key = tuple()
    string = str()

    while len(object_stack) > 0:

        if str(input()) == "y":

            break

        else:

            print(string)

        # print("strnested(obj={})".format(str(obj)))
        # print("object_stack: {}".format(object_stack))

        # check object

        if type(object_stack[-1]) in (bool, int, float, str) or \
           obj == None:

            # non-iterables

            if object_stack[-1] not in classes:

                # str(object_stack[-1])

                if len(cur_container_type) > 0:

                    if len(cur_container_key) > 0:
                    
                        string = string + "{}{}[{}, {}] {}\n".format(strlevelpadding(len(object_stack) - 1), cur_container_type, indices[-1], str(cur_container_key[0]), str(object_stack[-1]))

                    else:

                        string = string + "{}{}[{}] {}\n".format(strlevelpadding(len(object_stack) - 1), cur_container_type, indices[-1], str(object_stack[-1]))

                else:

                    string = string + "{}{}\n".format(strlevelpadding(len(object_stack) - 1), str(object_stack[-1]))

            else:

                # object allready str()-ed

                string = string + "{}{} (class has already str()-inged!)\n".format(strlevelpadding(len(object_stack) - 1), str(object_stack[-1]))

            del object_stack[-1]

        else:

            # iterables

            if len(indices) < len(object_stack):

                # object_stack[last] iteration not started yet

                indices.append(0)
                cur_container_type = strtype(object_stack[-1])
                string = string + "{}{}\n".format(strlevelpadding(len(object_stack) - 1), cur_container_type)
                

            if has_index(object_stack[-1], indices[-1]):

                # add next item from iterable

                if is_class(object_stack[-1]):

                    classes.add(object_stack[-1])

                if has_key(object_stack[-1]):

                    cur_container_key = get_key(object_stack[-1], indices[-1])
                
                object_stack.append(get_item(object_stack[-1], indices[-1]))

                indices[-1] += 1
                
            else:

                # no more items in iterable

                cur_container_key = tuple()
                cur_container_type = str()
                del indices[-1]
                del object_stack[-1]

    else:

        # No further objects

        return string


def has_index(obj=None, index=int()):

    if type(obj) in (set, frozenset, tuple, list, dict):

        if len(obj) > 0 and index < len(obj):

            return True

        else:

            return False

    elif hasattr(obj, "__dict__"):

        return has_index(obj.__dict__, index)

    else:

        raise TypeError(".has_index(obj={}, index={}) No result!".format(obj, index))


def get_item(obj=None, index=int()):

    if type(obj) in (tuple, list):

        return obj[index]

    elif type(obj) in (set, frozenset):

        return sorted(obj)[index]

    elif type(obj) == dict:

        return obj[sorted(obj.keys())[index]]

    elif hasattr(obj, "__dict__"):

        return obj[sorted(obj.__dict__.keys())[index]]

    else:

        raise TypeError("get_item(obj={}, index={})".format(obj, index))


def has_key(obj):

    if type(obj) == dict or hasattr(obj, "__dict__"):

        return True

    else:

        return False


def get_key(obj=None, index=int()):

    # -> No key: tuple()
    #    (key, )

    # print("get_key(obj={}, index={})".format(obj, index))

    if type(obj) == dict:

        return (sorted(obj.keys())[index], )

    elif hasattr(obj, "__dict__"):

        return get_key(obj.__dict__, index)

    else:

        return tuple()


def is_class(obj=None):

    if type(obj) not in (set, frozenset, tuple, list, dict) and \
       hasattr(obj, "__dict__"):

        return True

    else:

        return False



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
    
    # print(strclass(test_class))

    # print(strnested(tuple_test), "\n")

    # print(strnested(dict_test_0), "\n")

    print(strnested(nested_dict), "\n")

    # print(strnested(set_test), "\n")

    
