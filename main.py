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

    @classmethod
    def from_char(cls, char):
        return Color.letters_map()[char]

    @classmethod
    def letters(cls):
        return set(map(lambda c: c.get_color_letter(), cls))

    @classmethod
    def letters_map(cls):
        result = {}
        for c in Color:
            result[c.get_color_letter()] = c
        return result

    def __str__(self):
        return self.name

    def get_color_letter(self):
        return self.name[0].lower()


class Face:
    """Face contains of 9 elements with some colors"""

    def __init__(self, side, colors):
        self.side = side
        self.colors = []
        if isinstance(colors, str):
            for c in colors:
                self.colors.append(Color.from_char(c))
        else:
            self.colors = colors

    def __str__(self):
        return "{0}, colors: {1}".format(self.side, ','.join(map(str, self.colors)))


class Cube:
    """Simple data model of Rubik's Cube"""

    def __init__(self, faces):
        self.faces = faces

    def __str__(self):
        return '\n'.join(map(str, cube.faces))


# input cube faces
print("Input colors could be one of: " + str(Color.letters()))
faces = []
for s in Side:
    # TODO: check input values, string size and color letters
    colorsRaw = input("Input colors of {0} face ".format(s))
    face = Face(s, colorsRaw[:9])
    print(face)
    faces.append(face)

cube = Cube(faces)
print(str(cube))
