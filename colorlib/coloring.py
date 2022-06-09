import math

import colorlib


def _lerp_multi(range_min: tuple, range_max: tuple, prog):
    t = []
    for (v, v1) in zip(range_min, range_max):
        t.append(_lerp(v, v1, prog))
    return tuple(t)


def _lerp(range_min, range_max, prog):
    return range_min + (range_max - range_min) * prog


def _gen_circle_gradient(width: int, height: int, from_color: tuple[int, int, int], to_color: tuple[int, int, int],
                         radius: int, center_x_mul: float, center_y_mul: float):
    matrix = []
    center_x = width * center_x_mul
    center_y = height * center_y_mul
    for coord_y in range(height):
        matrix_row = []
        delta_y = abs(center_y - coord_y)
        for coord_x in range(width):
            delta_x = abs(center_x - coord_x)
            dist = math.sqrt(math.pow(delta_x, 2) + math.pow(delta_y, 2))
            fp = dist / float(radius)
            fp = max(0.0, min(1.0, fp))
            col = _lerp_multi(from_color, to_color, 1 - fp)
            matrix_row.append(
                (
                    math.floor(col[0]),
                    math.floor(col[1]),
                    math.floor(col[2])
                ))
        matrix.append(matrix_row)
    return matrix


def _gen_gradient(width: int, height: int, from_color: tuple[int, int, int], to_color: tuple[int, int, int],
                  degrees: int):
    normalized_degrees = degrees % 90  # only need 90 degrees to describe everything we need
    deg_vec = float(normalized_degrees) / 90.0
    matrix = []
    for coord_y in range(height):
        matrix_row = []
        progress_y = float(coord_y) / float(height - 1)
        start = _lerp_multi(from_color, to_color, progress_y * deg_vec)
        end = _lerp_multi(start, to_color, (1 - deg_vec))
        for coord_x in range(width):
            progress = float(coord_x) / float(width - 1)
            col = _lerp_multi(start, end, progress)
            matrix_row.append(
                (
                    math.floor(col[0]),
                    math.floor(col[1]),
                    math.floor(col[2])
                ))
        matrix.append(matrix_row)
    return matrix


def colorize_with_gradient(text: str, from_color: tuple[int, int, int], to_color: tuple[int, int, int],
                           degrees: int):
    """
    Colorizes a text with a specified gradient

    :param text: The text to generate the gradient from
    :param from_color: RGB of the starting color
    :param to_color: RGB of the end color
    :param degrees: The degrees of the gradient
    :return: A matrix with colors and the character they represent
    """
    lst = text.split("\n")
    width = 0
    height = len(lst)
    for line in lst:
        width = max(width, len(line))

    gradient = _gen_gradient(width, height, from_color, to_color, degrees)
    fin = []
    for y in range(len(gradient)):
        row = gradient[y]
        text_row = lst[y]
        fin_row = []
        for x in range(len(row)):
            if x >= len(text_row):
                break
            px = row[x]
            char = text_row[x]
            fin_row.append((char, px))
        fin.append(fin_row)
    return colorlib.ColorMatrix(fin)


def colorize_with_circle_gradient(text: str, from_color: tuple[int, int, int], to_color: tuple[int, int, int],
                                  radius: int, center_x: float = 0.5, center_y: float = 0.5):
    """
    Colorizes a text with a radial gradient

    :param text: The text to generate the gradient from
    :param from_color: RGB of the starting color
    :param to_color: RGB of the end color
    :param radius: The radius of the circle
    :param center_x: The X center of the circle (0-1)
    :param center_y: The Y center of the circle (0-1)
    :return: A matrix with colors and the character they represent
    """
    lst = text.split("\n")
    width = 0
    height = len(lst)
    for line in lst:
        width = max(width, len(line))

    gradient = _gen_circle_gradient(width, height, from_color, to_color, radius, center_x, center_y)
    fin = []
    for y in range(len(gradient)):
        row = gradient[y]
        text_row = lst[y]
        fin_row = []
        for x in range(len(row)):
            if x >= len(text_row):
                break
            px = row[x]
            char = text_row[x]
            fin_row.append((char, px))
        fin.append(fin_row)
    return colorlib.ColorMatrix(fin)
