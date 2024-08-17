

# datastructure_conversion_types

DSCT_truncated_line = 0
DSCT_line_per_value = 1

DSCT = DSCT_truncated_line




def str_class_attrs(instance=None):

    string = "{}\n\n".format(str(instance))

    for attr_key in dir(instance):

        if not callable(getattr(instance, attr_key)) and \
           type(getattr(instance, attr_key)) not in (tuple, list, set, frozenset, dict) and \
           attr_key[0:2] != "__":

            string = string + "{:16}{}\n".format(attr_key, getattr(instance, attr_key))

        else:

            pass

    string = string + "\n"

    for attr_key in dir(instance):

        if callable(getattr(instance, attr_key)):

            pass

        elif attr_key[0:2] == "__":

            pass

        elif type(getattr(instance, attr_key)) in (tuple, list):

            string = string + "{} ({})\n".format(attr_key, type(getattr(instance, attr_key)))

            if DSCT == DSCT_truncated_line:

                string = string + "{:.35}".format(str(getattr(instance, attr_key)))

            elif DSCT == DSCT_line_per_value:

                for i in range(len(getattr(instance, attr_key))):

                    string = string + " . {:2d} {}\n".format(i, getattr(instance, attr_key)[i])

            else:

                pass

            string = string + "\n"

        elif type(getattr(instance, attr_key)) in (set, frozenset):

            string = string + "{} ({})\n".format(attr_key, type(getattr(instance, attr_key)))

            for e in getattr(instance, attr_key):

                string = string + " . {}\n".format(e)

            string = string + "\n"

        elif type(getattr(instance, attr_key)) == dict:

            string = string + "{} ({})\n".format(attr_key, type(getattr(instance, attr_key)))

            for dict_key in getattr(instance, attr_key).keys():

                string = string + " . {:6} {}\n".format(str(dict_key), getattr(instance, attr_key)[dict_key])

            string = string + "\n"

        else:

            # string = string + "{:10}{}\n".format(attr_key, getattr(instance, attr_key))

            pass

    return string
