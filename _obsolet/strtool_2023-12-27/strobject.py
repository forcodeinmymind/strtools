

print("colors.__init__()\nname: {}\nfile: {}\n".format(__name__, __file__))


"""
str_object(obj=None) -> str, all nested objects in obj
"""

def is_nested(obj=None) -> bool:

    if isinstance(obj, bool) or \
       isinstance(obj, int) or \
       isinstance(obj, float) or \
       isinstance(obj, str) or \
       obj is None:

        return False

    else:

        return True


def __str_lvl_pad(level=int(), fillchar="·") -> str:

    return level * fillchar


def str_type(obj=None) -> str:

    str_type = str(type(obj))

    return str_type[str_type.find("'") + 1:-2]


def __str_nested(level=int(), obj=None, strcontainerkey=True, container_key=str(), fillchar="·") -> str:

    if strcontainerkey:

        return f"{__str_lvl_pad(level, fillchar)}[{container_key}] {str_type(obj)}\n"

    else:

        return f"{__str_lvl_pad(level, fillchar)}{str_type(obj)}\n"


def __str_value(level=int(), obj=None, strcontainerkey=True, container_key=str(), strtype=True, fillchar="·") -> str:

    if strcontainerkey and strtype:

        return f"{__str_lvl_pad(level, fillchar)}[{container_key}] {str_type(obj)}, {str(obj)}\n"

    elif not strcontainerkey and not strtype:

        return f"{__str_lvl_pad(level, fillchar)}{str(obj)}\n"

    elif strcontainerkey:

        return f"{__str_lvl_pad(level, fillchar)}[{container_key}] {str(obj)}\n"

    else:

        return f"{__str_lvl_pad(level, fillchar)}{str_type(obj)}, {str(obj)}\n"


def str_object(obj=None, strcontainerkey=True, strtype=True, fillchar=None) -> str:

    if fillchar == None:

        fillchar = "·"

    stack = [obj, ]
    indicies = list()
    classes = set()
    string = str()
    container_key = str()

    while len(stack):

        if not is_nested(stack[-1]):

            string += __str_value(len(stack) - 1, stack[-1], strcontainerkey, container_key, strtype, fillchar)
            del stack[-1]

        else:

            # nested objects

            if len(indicies) < len(stack):

                # setup stack[-1] iteration

                string += __str_nested(len(stack) - 1, stack[-1], strcontainerkey, container_key, fillchar)

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
                        
                        string += __str_value(len(stack) - 1, stack[-1], strcontainerkey, container_key, strtype, fillchar)
                        del stack[-1]

            else:

                # proceed stack[-1] iteration

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
                        container_key = str(indicies[-1])
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

                    # stack[-1] has .__dict__()

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



if __name__ == "__main__":

    pass
