import model.vertex as vertex
import model.graph as graph


class GraphGenerator(object):
    def __init__(self, movements, grid_limit):
        self.movements = movements
        self.grid_limit = grid_limit
        self.vertices = []
        self.edges = []

    def generate(self):
        self.vertices = self.generate_vertices()
        self.edges = self.generate_edges()
        return graph.Graph(self.vertices, self.edges)

    def generate_vertices(self):
        min_x = self.grid_limit.min_x
        max_x = self.grid_limit.max_x
        min_y = self.grid_limit.min_y
        max_y = self.grid_limit.max_y

        # one vertex per point in grid
        vertices = []
        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                vertices.append(vertex.Vertex(x, y))

        return vertices

    def generate_edges(self):
        # points in grid (graph's vertices) are connected by specific movements => edges
        edges = []
        for v in self.vertices:
            for m in self.movements:
                p = vertex.Vertex(v.x + m.incr_x, v.y + m.incr_y)
                if self.grid_limit.is_inside_grid(p):
                    edges.append((v.name, p.name, 1))
        return edges
