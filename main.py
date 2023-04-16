import turtle
from collections import deque

iterations : int = 10 
draw_each : bool = False

def parser(data: str):
    """
    Parses the data into individual commands
    
    The commands are:
    - f - forward
    - t - turn left
    - x - set x position
    - y - set y position
    - r - set rotation
    - c - set color
    - s - set size
    - u - pen up
    - d - pen down
    """
    commands = ["f", "t", "x", "y", "r", "c", "s", "u", "d"]
    parsed_data = []
    for i in data:
        if i in commands:
            parsed_data.append([i, ""])
        else:
            parsed_data[-1][1] += i

    return parsed_data

def deparser(data: list[list[str]]):
    """
    Turns the parsed data back into a string
    """
    return "".join([i[0] + i[1] for i in data])

def runner(data: list[list[str]], turtle: turtle.Turtle):
    """
    Runs the commands given by the parser
    """
    for command in data:
        match command[0]:
            case 'f':
                turtle.forward(int(command[1]))
            case 't':
                turtle.left(int(command[1]))
            case 'x':
                turtle.setx(int(command[1]))
            case 'y':
                turtle.sety(int(command[1]))
            case 'r':
                turtle.setheading(int(command[1]))
            case 'c':
                turtle.color(command[1].lower())
            case 's':
                turtle.pensize(int(command[1]))
            case 'u':
                turtle.penup()
            case 'd':
                turtle.pendown()
            case _:
                raise ValueError(f"Unknown command {command[0]}")

def mirror(data: str):
    data = parser(data)
    data = data[::-1]
    for i, (c, v) in enumerate(data):
        if c == "t":
            data[i][1] = str(-int(v))
    return deparser(data)

def gen_func(start: str = "f10"):
    for i in range(iterations):
        start = start + "t90" + mirror(start)
        print(start)
        yield start

t = turtle.Turtle()
s = t.getscreen()
 
#set everything up
t.speed(0)
runner(parser("r180"),t)

if draw_each:
    for i in gen_func():
        runner(parser(i), t)
else:
    last, = deque(gen_func(), 1)
    runner(parser(last), t)

# runner(parser("FLFLFRFLFLFRFRF".replace("F", "f10").replace("L", "t90").replace("R", "t-90")), t)

s.mainloop()
