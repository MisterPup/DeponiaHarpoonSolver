class Vertex(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.name = "({}, {})".format(x, y)

    def __eq__(self, other):
        if isinstance(other, Vertex):
            return self.x == other.x and self.y == other.y
        return False

    def __repr__(self):
        return self.name
