"""
Functions for normalization words
"""
import re

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l",
               "m", "n", "o", "p", "r", "s", "t", "u", "f", "h", "ts", "ch",
               "sh", "sch", "", "y", "", "e", "yu", "ja", "je", "i", "ji", "g")

TRANS = {}
for key, value in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS.update({ord(key): value})
    TRANS.update({ord(key.upper()): value.upper()})


def translate(name):
    """
    Translate word into latin
    """
    t_name = ''
    for char in name:
        t_name += TRANS.get(ord(char), char)
    return t_name


def normalize(name):
    """
    Translate word into latin and replace all symbols except alphabet or
    numbers to '_'
    :param name: str
    :return: str
    """
    name = translate(name)
    name = re.sub(r'\W', '_', name)
    return name
