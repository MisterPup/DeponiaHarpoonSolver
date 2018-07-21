
class GridLimit(object):
    def __init__(self, min_x, max_x, min_y, max_y):
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y

    def is_inside_grid(self, p):
        return self.min_x <= p.x <= self.max_x and self.min_y <= p.y <= self.max_y

