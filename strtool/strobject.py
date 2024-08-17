"""
Create a suitable str representativ
for the individual in python objects.

Functions
---------

str_globals
    Return a str objects in globals()
    Obsolet!

str_dir
    Return str dir(object)

str_dict
    Return str of dict

str_overwrite
    Return replaced str('_object') of defined type('_object')
"""

__all__ = ("str_dir", "str_class", "str_dict")


def str_globals() -> str:
    """
    Obsolet
    global() is called in strobject.py
    not in model in witch it is imported!
    Use instead: str_dict(globals())
    """
    string = f"{__name__}.str_globals()\n"
    _dict = dict()
    for name in globals():
        _dict[name] = globals()[name]
        string += str_dict(_dict)
    return string

def str_dir(_object) -> str:
    """
    Return str of argument dir('_object')
    """
    string = f".str_dir({_object=})\n"
    for name in dir(_object):
        string += f"{name}\n"
    return string

def str_class(instance) -> str:
    """
    Return str of argument 'instance'
    """
    string = f".str_class({instance=})\n"
    _dict = dict()
    for name in dir(instance):
        _dict[name] = getattr(instance, name)
    string += str_dict(_dict)
    return string

def str_dict(_dict: dict) -> str:
    """
    Return a string of argument '_dict'
    """
    if isinstance(_dict, dict):
        string = f".str_dict()\n"
        string = str()
        pad = 2 + max(len(str(key)) for key in _dict)
        for key in _dict:
            string += f"{str(key):<{pad}}{type(_dict[key])}\n"
        return string
    else:
        raise TypeError(f".str_dict(); isinstance({_dict=}, dict)=False")

def str_overwrite(_object) -> str:
    """
    Overwrite the str(objects) of defined objects
    """
    if str(_object)[1:len("<module")] == "module":
        module_name = str(_object).split()[1].replace("'")
        return f"<module {module_name}>"
    else:
        return _object


if __name__ == "__main__":
    print(str_globals())
    print(str_dir(__builtins__))
