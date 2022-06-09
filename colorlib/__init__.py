class ColorMatrix:
    """
    A matrix of colored characters
    """
    def __init__(self, matrix: list[list[tuple[str, tuple[int, int, int]]]]):
        """
        Initializes the matrix

        :param matrix: A 2 dimensional array of colored elements
        """
        self.matrix = matrix

    def get_matrix(self):
        """
        Gets this matrix

        :return: A 2 dimensional array representing this matrix
        """
        return self.matrix

    @staticmethod
    def _to_ansi_color(text: str, color: tuple[int, int, int]):
        return f"\x1b[38;2;{color[0]};{color[1]};{color[2]}m{text}"

    def to_ansi_escape_sequences(self):
        """
        Converts the matrix to an ansi escape sequence you can print out to the terminal. Requires truecolor support

        :return: A string of ansi escape codes representing this matrix
        """
        f = []
        for row in self.get_matrix():
            f.append("".join([ColorMatrix._to_ansi_color(x[0], x[1]) for x in row]))
        return "\n".join(f)
