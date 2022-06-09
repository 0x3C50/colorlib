from colorlib import text_manipulation
from enum import Enum


class BoxType:
    def __init__(self, left_top: str, right_top: str, left_bottom: str, right_bottom: str, vertical: str,
                 horizontal: str):
        self.left_top = left_top
        self.right_top = right_top
        self.left_bottom = left_bottom
        self.right_bottom = right_bottom
        self.vertical = vertical
        self.horizontal = horizontal


class BoxTypes(Enum):
    normal = BoxType("┌", "┐", "└", "┘", "│", "─")
    light = BoxType("┌", "┐", "└", "┘", " ", " ")
    double = BoxType("╔", "╗", "╚", "╝", "║", "═")
    rounded = BoxType("╭", "╮", "╰", "╯", "│", "─")
    thick = BoxType("┏", "┓", "┗", "┛", "┃", "━")


def generate_text_box(text: str, box_type: BoxType = BoxTypes.normal.value, padding_x: int = 1, padding_y: int = 0):
    lines = text_manipulation.make_text_block(text).split("\n")
    lines_fin = [f"{box_type.left_top}{box_type.horizontal * (padding_x * 2 + len(lines[0]))}{box_type.right_top}"]
    for i in range(padding_y):
        lines_fin.append(f"{box_type.vertical}{' ' * (padding_x * 2 + len(lines[0]))}{box_type.vertical}")
    for i in lines:
        lines_fin.append(f"{box_type.vertical}{' ' * padding_x}{i}{' ' * padding_x}{box_type.vertical}")
    for i in range(padding_y):
        lines_fin.append(f"{box_type.vertical}{' ' * (padding_x * 2 + len(lines[0]))}{box_type.vertical}")
    lines_fin.append(
        f"{box_type.left_bottom}{box_type.horizontal * (padding_x * 2 + len(lines[0]))}{box_type.right_bottom}")
    return "\n".join(lines_fin)


def generate_cowsay(text: str):
    lines = text_manipulation.make_text_block(text).split("\n")
    wid = len(lines[0]) + 2
    lines_fin = [
        f" {'-' * wid}"
    ]
    for i in range(len(lines)):
        prefix = "<"
        suffix = ">"
        if len(lines) > 1:
            if i == 0:
                prefix = "/"
                suffix = "\\"
            elif i == len(lines) - 1:
                prefix = "\\"
                suffix = "/"
            else:
                prefix = "|"
                suffix = "|"
        line = lines[i]
        lines_fin.append(f"{prefix} {line} {suffix}")
    lines_fin.append(f" {'-' * wid}")
    lines_fin.append("        \\   ^__^")
    lines_fin.append("         \\  (oo)\\_______")
    lines_fin.append("            (__)\\       )\\/\\")
    lines_fin.append("                ||----w |")
    lines_fin.append("                ||     ||")
    return "\n".join(lines_fin)
