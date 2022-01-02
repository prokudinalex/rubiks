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

    def __init__(self, colors):
        self.colors = []
        self.size = 3
        if isinstance(colors, str):
            for c in colors:
                self.colors.append(Color.from_char(c))
        else:
            self.colors = colors

    def __str__(self):
        return "{0}\n{1}\n{2}" \
            .format('\t'.join(map(str, map(lambda c: c.get_color_letter(), self.get_row(0)))),
                    '\t'.join(map(str, map(lambda c: c.get_color_letter(), self.get_row(1)))),
                    '\t'.join(map(str, map(lambda c: c.get_color_letter(), self.get_row(2)))))

    def get_row(self, i):
        # TODO: check input indexes
        return [self.colors[i * self.size], self.colors[i * self.size + 1], self.colors[i * self.size + 2]]


class Cube:
    """Simple data model of Rubik's Cube"""

    def __init__(self, faces):
        self.faces = faces

    def __str__(self):
        return '\n'.join(map(lambda x: "---{0}---\n{1}".format(x[0], x[1]), self.faces.items()))

    @staticmethod
    def __cube_clockwise_sides(side):
        if side == Side.Up:
            return [Side.Front, Side.Right, Side.Back, Side.Left]
        elif side == Side.Bottom:
            return [Side.Front, Side.Left, Side.Back, Side.Right]
        elif side == Side.Front:
            return [Side.Up, Side.Left, Side.Bottom, Side.Right]
        elif side == Side.Back:
            return [Side.Up, Side.Right, Side.Bottom, Side.Left]
        elif side == Side.Left:
            return [Side.Up, Side.Back, Side.Bottom, Side.Front]
        elif side == Side.Right:
            return [Side.Up, Side.Front, Side.Bottom, Side.Back]

    @staticmethod
    def __cube_rotation_sides(side, clockwise):
        if clockwise:
            return Cube.__cube_clockwise_sides(side)
        else:
            sides = Cube.__cube_clockwise_sides(side)
            tmp = sides[1]
            sides[1] = sides[3]
            sides[3] = tmp
            return sides

    def rotate_cube(self, side, clockwise=True):
        print("Rotate cube from side {0} with clockwise {1}".format(side, clockwise))
        sides = Cube.__cube_rotation_sides(side, clockwise)
        print("Sides to rotate: {0}".format(sides))
        tmp = self.faces[sides[0]]
        self.faces[sides[0]] = self.faces[sides[1]]
        self.faces[sides[1]] = self.faces[sides[2]]
        self.faces[sides[2]] = self.faces[sides[3]]
        self.faces[sides[3]] = tmp
        # TODO: rotate elements inside "side" and "mirror side"


# input cube faces
print("Input colors could be one of: " + str(Color.letters()))
# faces = []
# for s in Side:
#     # TODO: check input values, string size and color letters
#     colorsRaw = input("Input colors of {0} face ".format(s))
#     face = Face(s, colorsRaw[:9])
#     print(face)
#     faces.append(face)

inputFaces = {
    Side.Front: Face("rrrrrrrrr"),
    Side.Right: Face("ggggggggg"),
    Side.Back: Face("ooooooooo"),
    Side.Left: Face("bbbbbbbbb"),
    Side.Up: Face("yyyyyyyyy"),
    Side.Bottom: Face("wwwwwwwww")
}
cube = Cube(inputFaces)
print("\n\nYour Cube:\n" + str(cube))

cube.rotate_cube(Side.Up)
cube.rotate_cube(Side.Front)
cube.rotate_cube(Side.Front)
cube.rotate_cube(Side.Up)
cube.rotate_cube(Side.Left, False)
cube.rotate_cube(Side.Right, False)
cube.rotate_cube(Side.Right)
cube.rotate_cube(Side.Bottom)
cube.rotate_cube(Side.Back)
cube.rotate_cube(Side.Up, False)

print("\n\nYour Cube After rotate:\n" + str(cube))
