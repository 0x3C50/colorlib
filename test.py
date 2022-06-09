import colorlib.boxes
import colorlib.coloring

a = """this is the first text
with newline shit
and stuff
very cool
qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq"""

print(
    colorlib.coloring.colorize_with_circle_gradient(
        colorlib.boxes.generate_cowsay(a), (255, 50, 50),
        (50, 255, 50), 30).to_ansi_escape_sequences()
)
