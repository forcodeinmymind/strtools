

print("colors.__init__()\nname: {}\nfile: {}\n".format(__name__, __file__))

"""
import sys
import os
sys.path.append(os.path.join("E:/Programmieren/Python/Module"))
import logger
"""


__fillchar = "·"
__do_strtype = False
__strnamespace = False
__strnested = True



def set_do_strtype(state=True):

    global __do_strtype

    __do_strtype = state


def set_fillchar(fillchar="·"):

    global __fillchar

    __fillchar = fillchar="·"


def set_strnested(state=True):

    global __strnested

    __strnested = state


def __str_lvl_pad(level=int()):

    return level * __fillchar


def str_type(obj=None):

    str_type = str(type(obj))

    return str_type[str_type.find("'") + 1:-2]


def str_nested(obj=None):

    stack = [obj, ]
    indicies = list()
    classes = set()
    string = str()

    container_type = str()
    container_key = str()

    while len(stack):

        if not is_nested(stack[-1]):

            # string = string + strnestedobject(len(stack) - 1, stack[-1], container_key)
            string = string + str_value(len(stack) - 1, stack[-1], container_key)

            del stack[-1]

        else:

            # nested objects

            if len(indicies) < len(stack):

                # str(stack[-1]) -> str collection
                # string = string + strnestedobject(len(stack) - 1, stack[-1], container_key)
                string = string + str_nested(len(stack) - 1, stack[-1], container_key)

                if isinstance(stack[-1], set) or \
                   isinstance(stack[-1], frozenset):

                    indicies.append(tuple(stack[-1]))
                
                elif isinstance(stack[-1], tuple) or \
                     isinstance(stack[-1], list):

                    indicies.append(int())

                elif isinstance(stack[-1], dict):

                    indicies.append(tuple(stack[-1].keys()))

                else:

                    if hasattr(stack[-1], "__dict__"):

                        if stack[-1] in classes:

                            string = string[ :-1] + " [Has already iterated]\n"

                            del stack[-1]

                        else:

                            indicies.append(tuple(stack[-1].__dict__.keys()))
                            classes.add(stack[-1])

                    else:

                        # str(stack[-1]) -> str class: has already iterated

                        # indicies.append(tuple())

                        # raise TypeError()

                        # -> pygame.Rect()

                        # string = string + strnestedobject(len(stack) - 1, stack[-1], container_key)
                        string = string + str_value(len(stack) - 1, stack[-1], container_key)

                        del stack[-1]

            else:

                if isinstance(stack[-1], set) or \
                   isinstance(stack[-1], frozenset):

                    if len(indicies[-1]):

                        stack.append(indicies[-1][-1])
                        indicies[-1] = indicies[-1][0:-1]
                        container_key = str()

                    else:

                        del stack[-1]
                        del indicies[-1]
                        container_key = str()

                elif isinstance(stack[-1], tuple) or \
                     isinstance(stack[-1], list):

                    if indicies[-1] < len(stack[-1]):

                        stack.append(stack[-1][indicies[-1]])
                        container_key = str()
                        indicies[-1] += 1

                    else:

                        del stack[-1]
                        del indicies[-1]
                        container_key = str()

                elif isinstance(stack[-1], dict):

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


def is_nested(obj=None):

    if isinstance(obj, bool) or \
       isinstance(obj, int) or \
       isinstance(obj, float) or \
       isinstance(obj, str) or \
       obj is None:

        return False

    else:

        return True

def str_nested(level=int(), obj=None, container_key=str()):

    return f"{__str_lvl_pad(level)}[{container_key}] {str_type(obj)}\n"


def str_value(level=int(), obj=None, container_key=str()):

    return f"{__str_lvl_pad(level)}[{container_key}] {str_type(obj)}, {str(obj)}\n"





if __name__ == "__main__":

    pass
