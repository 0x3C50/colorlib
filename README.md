# Colorlib
A library designed for making working with terminal user interfaces easier

## Features
Colorlib can
- Handle colors for you
- Generate boxes
- Manipulate text alignment
- And more

### Key features
#### Colors
Colorlibis designed to make coloring elements a bit easier. You can color logos, ansi art or whatever you'd like and print that out to a terminal. Here's a demo
```python
import colorlib.coloring

logo = """
  ██████  ▄▄▄       ███▄ ▄███▓ ██▓███   ██▓    ▓█████    ▄▄▄█████▓▓█████ ▒██   ██▒▄▄▄█████▓
▒██    ▒ ▒████▄    ▓██▒▀█▀ ██▒▓██░  ██▒▓██▒    ▓█   ▀    ▓  ██▒ ▓▒▓█   ▀ ▒▒ █ █ ▒░▓  ██▒ ▓▒
░ ▓██▄   ▒██  ▀█▄  ▓██    ▓██░▓██░ ██▓▒▒██░    ▒███      ▒ ▓██░ ▒░▒███   ░░  █   ░▒ ▓██░ ▒░
  ▒   ██▒░██▄▄▄▄██ ▒██    ▒██ ▒██▄█▓▒ ▒▒██░    ▒▓█  ▄    ░ ▓██▓ ░ ▒▓█  ▄  ░ █ █ ▒ ░ ▓██▓ ░ 
▒██████▒▒ ▓█   ▓██▒▒██▒   ░██▒▒██▒ ░  ░░██████▒░▒████▒     ▒██▒ ░ ░▒████▒▒██▒ ▒██▒  ▒██▒ ░ 
▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░░ ▒░   ░  ░▒▓▒░ ░  ░░ ▒░▓  ░░░ ▒░ ░     ▒ ░░   ░░ ▒░ ░▒▒ ░ ░▓ ░  ▒ ░░   
░ ░▒  ░ ░  ▒   ▒▒ ░░  ░      ░░▒ ░     ░ ░ ▒  ░ ░ ░  ░       ░     ░ ░  ░░░   ░▒ ░    ░    
░  ░  ░    ░   ▒   ░      ░   ░░         ░ ░      ░        ░         ░    ░    ░    ░      
      ░        ░  ░       ░                ░  ░   ░  ░               ░  ░ ░    ░           
"""

print(colorlib.coloring.colorize_with_gradient(logo, (2, 45, 189), (189, 2, 99), 45).to_ansi_escape_sequences())
```
![img.png](images/img.png)

You can also make radial gradients, like this
```python
import colorlib.coloring

logo = """
  ██████  ▄▄▄       ███▄ ▄███▓ ██▓███   ██▓    ▓█████    ▄▄▄█████▓▓█████ ▒██   ██▒▄▄▄█████▓
▒██    ▒ ▒████▄    ▓██▒▀█▀ ██▒▓██░  ██▒▓██▒    ▓█   ▀    ▓  ██▒ ▓▒▓█   ▀ ▒▒ █ █ ▒░▓  ██▒ ▓▒
░ ▓██▄   ▒██  ▀█▄  ▓██    ▓██░▓██░ ██▓▒▒██░    ▒███      ▒ ▓██░ ▒░▒███   ░░  █   ░▒ ▓██░ ▒░
  ▒   ██▒░██▄▄▄▄██ ▒██    ▒██ ▒██▄█▓▒ ▒▒██░    ▒▓█  ▄    ░ ▓██▓ ░ ▒▓█  ▄  ░ █ █ ▒ ░ ▓██▓ ░ 
▒██████▒▒ ▓█   ▓██▒▒██▒   ░██▒▒██▒ ░  ░░██████▒░▒████▒     ▒██▒ ░ ░▒████▒▒██▒ ▒██▒  ▒██▒ ░ 
▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░░ ▒░   ░  ░▒▓▒░ ░  ░░ ▒░▓  ░░░ ▒░ ░     ▒ ░░   ░░ ▒░ ░▒▒ ░ ░▓ ░  ▒ ░░   
░ ░▒  ░ ░  ▒   ▒▒ ░░  ░      ░░▒ ░     ░ ░ ▒  ░ ░ ░  ░       ░     ░ ░  ░░░   ░▒ ░    ░    
░  ░  ░    ░   ▒   ░      ░   ░░         ░ ░      ░        ░         ░    ░    ░    ░      
      ░        ░  ░       ░                ░  ░   ░  ░               ░  ░ ░    ░           
"""

print(colorlib.coloring.colorize_with_circle_gradient(logo, (2, 45, 189), (189, 2, 99), 60, 0.4, 0.2).to_ansi_escape_sequences())
```
![img.png](images/img2.png)
#### Box generation
Colorlib can generate boxes for you, for text you input. An example:
```python
import colorlib.boxes

logo = """This text is multiline
I can type whatever I want and the box will fit it
This is a nice library"""

print(colorlib.boxes.generate_text_box(logo, colorlib.boxes.BoxTypes.rounded.value))
```
![img.png](images/img3.png)
You can also change the box layout, see BoxType in boxes.py
#### Manipulate text alignment
Colorlib can also help you align text, here's an example
```python
import colorlib.text_manipulation

logo = """This text is centered
It is centered because I want it to be
Very nice, will fit whatever"""

print(colorlib.text_manipulation.center_text_in_itself(logo))
```
![img.png](images/img4.png)
You can also right align text:
```python
import colorlib.text_manipulation

logo = """This text is right aligned
Just because, no particular reason
Nice weather outside today, isn't it?"""

print(colorlib.text_manipulation.right_align_text(logo))
```
![img.png](images/img5.png)
There are many more features, the api is pretty self explanatory.

# Support
You can show your support by leaving a star on this repo, which would help me out a lot! Also, if you find any bugs, don't hesitate to open up an issue for it.