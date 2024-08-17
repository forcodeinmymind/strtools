import os
import sys

from datetime import datetime



# unicode, char

def gen_unicode_chars(start=0, end=None):

    # -> generator with strings of chars

    i = start

    while True:

        if end != None:

            if i >= end:

                break

        try:

            yield chr(i)

            i += 1

        except:

            break;


def export_chars(start=0, end=None, filename="unicode.txt"):

    with open(filename, 'w') as obj_file:

        obj_file.write("{}".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

        i = 0

        for char in gen_unicode_chars(start, end):

            try:

                obj_file.write("{:08d} {}\n".format(i, str(char)))

            except:

                # save chr not available in *.txt format
                # obj_file.write("{:07d} n/a\n".format(i))

                pass

            i += 1


def import_chars(filename="unicode.txt"):

    # -> str(), alle chrs in file

    str_chars = str()

    if os.path.isfile(str(filename)):

        with open(filename, 'r') as obj_file:

            data = obj_file.read()

            for line in data.split("\n"):

                try:

                    str_chars = str_chars + line[line.index(' ') + 1: ]

                except:

                    pass

        return str_chars

    else:

        raise RuntimeError("file '{}' don't exist!".format(filename))


# string info's

def str_char_table(font=None, str_chars=str()):

    # -> str()

    str_table = str()

    metrics = font.get_metrics(str_chars)

    for i in range(len(str_chars)):

        metric = metrics[i]
        r_char = font.get_rect(str_chars[i])

        if metrics[i] == None:

            metric = 6 * ("n/a", )

        str_table = str_table + "index: {:3d}   char: {:>3}   unicode: {:3d}  min_x: {:>3}   max_x: {:>3}   min_y: {:>3}   max_y: {:>3}   h_adv: {:>3}   v_adv: {:>3}   x: {:3d}   y: {:3d}   w: {:3d}   h: {:3d}\n".format(i, str_chars[i], ord(str_chars[i]), str(metric[0]), str(metric[1]), str(metric[2]), str(metric[3]), str(metric[4]), str(metric[5]), *r_char.topleft, *r_char.size)

    return str_table


# print

def print_unicode(start=0, end=None):

    i = start

    for char in gen_unicode_chars(start, end):

        try:

            print("index: {:10d}   char: {:3}".format(i, chr(i)))

            i += 1

        except:

            break


if __name__ == "__main__":

    import pygame
    import pygame.freetype

    pygame.init()
    pygame.freetype.init()

    font0 = pygame.freetype.SysFont(None, 128)

    export_chars()

    str_chars = import_chars()

    print(str_char_table(font0, str_chars))
