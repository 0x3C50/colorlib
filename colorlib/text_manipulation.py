import math


def center_text(text: str, width: int):
    """
    Centers the text absolutely

    :param text: The text to center. Can be multiline
    :param width: The width to center the text to
    :return: The input text padded with spaces to make it centered relative to the width provided
    """
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
    """
    Centers text in itself

    :param text: The input text
    :return: The input text, but each line is padded to make it center aligned
    """
    width_of_text = 0
    lines = text.split("\n")
    for line in lines:
        width_of_text = max(width_of_text, len(line))
    padded_lines = [
        " " * int((width_of_text - len(x)) / 2) + x for x in lines
    ]
    return "\n".join(padded_lines)


def make_text_block(text: str):
    """
    Pads out each line to make the text even length

    :param text: The input text
    :return: The input text, but each line is padded with spaces
    """
    width_of_text = 0
    lines = text.split("\n")
    for line in lines:
        width_of_text = max(width_of_text, len(line))
    return "\n".join([
        x + " " * (width_of_text - len(x)) for x in lines
    ])


def right_align_text(text: str):
    """
    Aligns text to the right

    :param text: The input text
    :return: The input text, but each line is padded at the start to align the text to the right
    """
    width_of_text = 0
    lines = text.split("\n")
    for line in lines:
        width_of_text = max(width_of_text, len(line))
    padded_lines = [
        " " * int((width_of_text - len(x))) + x for x in lines
    ]
    return "\n".join(padded_lines)


def append_ascii(text_a: str, text_b: str, padding: int):
    """
    Appends two multiline strings center to center

    :param text_a: The starting text. Has to be larger or the same size than text_b
    :param text_b: The ending text to append to text_a
    :param padding: How much padding to use between the two
    :return: The result of appending the two texts
    """
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
