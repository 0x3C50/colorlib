import math


def center_text(text: str, width: int):
    width_of_text = 0
    lines = text.split("\n")
    for line in lines:
        width_of_text = max(width_of_text, len(line))
    if width % 2 == 1:
        width += 1
    div2 = int(width / 2 - width_of_text / 2)
    padded_lines = [
        " " * div2 + x for x in lines
    ]
    return "\n".join(padded_lines)


def center_text_in_itself(text: str):
    width_of_text = 0
    lines = text.split("\n")
    for line in lines:
        width_of_text = max(width_of_text, len(line))
    padded_lines = [
        " " * int((width_of_text - len(x)) / 2) + x for x in lines
    ]
    return "\n".join(padded_lines)


def make_text_block(text: str):
    width_of_text = 0
    lines = text.split("\n")
    for line in lines:
        width_of_text = max(width_of_text, len(line))
    return "\n".join([
        x + " " * (width_of_text - len(x)) for x in lines
    ])


def right_align_text(text: str):
    width_of_text = 0
    lines = text.split("\n")
    for line in lines:
        width_of_text = max(width_of_text, len(line))
    padded_lines = [
        " " * int((width_of_text - len(x))) + x for x in lines
    ]
    return "\n".join(padded_lines)


def append_ascii(text_a: str, text_b: str, padding: int):
    lines_a = make_text_block(text_a).split("\n")
    lines_b = text_b.split("\n")
    height_a = len(lines_a)
    height_b = len(lines_b)
    if height_b > height_a:
        raise ValueError(f"{height_b} > {height_a}")
    delta = height_a - height_b
    delta_half = math.ceil(delta / 2)
    for i in range(delta_half):
        lines_b.insert(0, " ")
        lines_b.append(" ")
    finished = [
        a + " " * padding + b for (a, b) in zip(lines_a, lines_b)
    ]
    return "\n".join(finished)
