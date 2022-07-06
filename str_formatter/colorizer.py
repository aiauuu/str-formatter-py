from typing import Union

def colorize(target_str: str, color: Union[list, str]=None, format: str=None):

    footer = "\033[0m"

    color_dict = {
        "black": "\033[30m",
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m",
        "default": "\033[39m",
        "bg_black": "\033[40m",
        "bg_red": "\033[41m",
        "bg_green": "\033[42m",
        "bg_yellow": "\033[43m",
        "bg_blue": "\033[44m",
        "bg_magenta": "\033[45m",
        "bg_cyan": "\033[46m",
        "bg_white": "\033[47m",
        "bg_default": "\033[49m",
        "reset": "\033[0m",
    }

    format_dict = {
        "bold": "\033[1m",
        "underline": "\033[4m",
        "invisible": "\033[08m",
        "reverse": "\033[07m",
    }

    return_str = target_str

    if type(color) in (list, tuple):
        rgb_color_header = "\033[38;2;{0[0]};{0[1]};{0[2]}m".format(color)
        return_str = f"{rgb_color_header}{target_str}{footer}"

    if type(color) is str:
        return_str = f"{color_dict[color]}{target_str}{footer}"
    
    if format is not None:
        return_str = f"{format_dict[format]}{return_str}{footer}"

    return return_str