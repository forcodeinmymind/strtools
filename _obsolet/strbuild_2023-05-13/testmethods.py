



def add_line(text=str(), str_line="this is a new test line"):

    len_text = text.count("\n")

    return text + "[{:04d}]{}\n".format(len_text, str_line)
