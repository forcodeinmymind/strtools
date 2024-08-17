

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


def strnested(obj=None):

    stack = [obj, ]
    indicies = list()
    classes = set()
    string = str()

    container_type = str()
    container_key = str()

    while len(stack):

        if type(stack[-1]) in (bool, int, float, str) or \
           stack[-1] is None:

            #not hasattr(stack[-1], "__dict__"):

            # non-iterables

            # str(stack[-1])
            string = string + strnestedobject(len(stack) - 1, stack[-1], container_key)

            del stack[-1]

        else:

            # iterables

            if len(indicies) < len(stack):

                # str(stack[-1]) -> str collection
                string = string + strnestedobject(len(stack) - 1, stack[-1], container_key)

                if type(stack[-1]) in (set, frozenset):

                    indicies.append(tuple(stack[-1]))
                
                elif type(stack[-1]) in (tuple, list):

                    indicies.append(int())

                elif type(stack[-1]) == dict:

                    indicies.append(tuple(stack[-1].keys()))

                else:

                    if hasattr(stack[-1], "__dict__"):

                        if stack[-1] in classes:

                            # str(stack[-1]) -> str class: has already iterated
                            string = string + strnestedobject(len(stack) - 1, stack[-1], container_key)[0:-1] + " Already str()\n"

                        else:

                            indicies.append(tuple(stack[-1].__dict__.keys()))
                            classes.add(stack[-1])

                    else:

                        # str(stack[-1]) -> str class: has already iterated

                        # indicies.append(tuple())

                        raise TypeError()

                        # -> pygame.Rect()

            else:

                if type(stack[-1]) in (set, frozenset):

                    if len(indicies[-1]):

                        stack.append(indicies[-1][-1])
                        indicies[-1] = indicies[-1][0:-1]
                        container_key = str()

                    else:

                        del stack[-1]
                        del indicies[-1]
                        container_key = str()

                elif type(stack[-1]) in (tuple, list):

                    if indicies[-1] < len(stack[-1]):

                        stack.append(stack[-1][indicies[-1]])
                        container_key = str()
                        indicies[-1] += 1

                    else:

                        del stack[-1]
                        del indicies[-1]
                        container_key = str()

                elif type(stack[-1]) == dict:

                    if len(indicies[-1]):

                        stack.append(stack[-1][indicies[-1][-1]])
                        container_key = str(indicies[-1][-1])
                        indicies[-1] = indicies[-1][0:-1]

                    else:

                        del stack[-1]
                        del indicies[-1]
                        container_key = str()

                else:

                    if len(indicies[-1]):

                        stack.append(getattr(stack[-1], indicies[-1][-1]))
                        container_key = str(indicies[-1][-1])
                        indicies[-1] = indicies[-1][0:-1]

                    else:

                        del stack[-1]
                        del indicies[-1]
                        container_key = str()

    else:

        return string




def strnestedobject(level=int(), obj=None, container_key=str()):

    if type(obj) in (bool, int, float, str) or \
       type(obj) == None:

        return "{}[{}] {}, {}\n".format(strlevelpadding(level), container_key, strtype(obj), str(obj))

    else:

        return "{}[{}] {}\n".format(strlevelpadding(level), container_key, strtype(obj))



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

    # print(strnested(nested_dict), "\n")

    # print(strnested(set_test), "\n")
    
    print(strnested(nested_dict), "\n")

    print(strnested(test_class), "\n")
    
