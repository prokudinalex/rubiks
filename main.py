from enum import Enum


class Side(Enum):
    Front = 1
    Right = 2
    Back = 3
    Left = 4
    Up = 5
    Bottom = 6

    def __str__(self):
        return self.name


class Color(Enum):
    White = 1
    Orange = 2
    Yellow = 3
    Red = 4
    Green = 5
    Blue = 6

    def __str__(self):
        return self.name


class Face:
    """Face contains of 9 elements with some colors"""

    def __init__(self, side, colors):
        self.side = side
        self.colors = colors

    def __str__(self):
        return "{0}, colors: {1}".format(self.side, ','.join(map(str, self.colors)))


class Cube:
    """Simple data model of Rubik's Cube"""

    def __init__(self):
        front = Face(Side.Front, [Color.White, Color.Blue, Color.Orange])
        right = Face(Side.Right, [])
        back = Face(Side.Back, [])
        left = Face(Side.Left, [])
        up = Face(Side.Up, [])
        bottom = Face(Side.Bottom, [])
        self.faces = [front, right, back, left, up, bottom]

    def __str__(self):
        return '\n'.join(map(str, cube.faces))


cube = Cube()
print(str(cube))
