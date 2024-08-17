

print("colors.__init__()\nname: {}\nfile: {}\n".format(__name__, __file__))

import sys
import os
sys.path.append(os.path.join("E:/Programmieren/Python/Module"))
import log



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

    pass
