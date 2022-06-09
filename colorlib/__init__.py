class ColorMatrix:
    def __init__(self, matrix: list[list[tuple[str, tuple[int, int, int]]]]):
        self.matrix = matrix

    def get_matrix(self):
        return self.matrix

    @staticmethod
    def _to_ansi_color(text: str, color: tuple[int, int, int]):
        return f"\x1b[38;2;{color[0]};{color[1]};{color[2]}m{text}"

    def to_ansi_escape_sequences(self):
        f = []
        for row in self.get_matrix():
            f.append("".join([ColorMatrix._to_ansi_color(x[0], x[1]) for x in row]))
        return "\n".join(f)
