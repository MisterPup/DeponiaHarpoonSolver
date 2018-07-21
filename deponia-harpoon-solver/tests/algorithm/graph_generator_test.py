import unittest
import algorithm.graph_generator as graph_generator
import model.grid_limit as grid_limit
import model.vertex as vertex
import model.movement as movement


class GraphGeneratorTest(unittest.TestCase):
    def test_given_one_point_then_generate_grid_one_vertex(self):
        limit = grid_limit.GridLimit(0, 0, 0, 0)

        generator = (
            graph_generator.GraphGenerator([], limit))
        vertices = generator.generate_vertices()

        self.assertEqual(vertex.Vertex(0, 0), vertices[0])

    def test_given_four_points_then_generate_grid_four_vertices(self):
        limit = grid_limit.GridLimit(0, 1, 0, 1)

        generator = (
            graph_generator.GraphGenerator([], limit))
        vertices = generator.generate_vertices()

        self.assertEqual(vertex.Vertex(0, 0), vertices[0])
        self.assertEqual(vertex.Vertex(0, 1), vertices[1])
        self.assertEqual(vertex.Vertex(1, 0), vertices[2])
        self.assertEqual(vertex.Vertex(1, 1), vertices[3])

    def test_given_six_points_then_generate_grid_six_vertices(self):
        limit = grid_limit.GridLimit(0, 2, 0, 1)

        generator = (
            graph_generator.GraphGenerator([], limit))
        vertices = generator.generate_vertices()

        self.assertEqual(vertex.Vertex(0, 0), vertices[0])
        self.assertEqual(vertex.Vertex(0, 1), vertices[1])
        self.assertEqual(vertex.Vertex(1, 0), vertices[2])
        self.assertEqual(vertex.Vertex(1, 1), vertices[3])
        self.assertEqual(vertex.Vertex(2, 0), vertices[4])
        self.assertEqual(vertex.Vertex(2, 1), vertices[5])

    def test_given_two_points_two_movements_then_generate_grid_two_vertices_two_edges(self):
        limit = grid_limit.GridLimit(0, 0, 0, 1)
        movements = [movement.Movement(0, 1), movement.Movement(0, -1)]

        generator = (
            graph_generator.GraphGenerator(movements, limit))
        graph = generator.generate()

        self.assertEqual(vertex.Vertex(0, 0), graph.vertices[0])
        self.assertEqual(vertex.Vertex(0, 1), graph.vertices[1])
        self.assertEqual((vertex.Vertex(0, 0).name, vertex.Vertex(0, 1).name, 1), graph.edges[0])
        self.assertEqual((vertex.Vertex(0, 1).name, vertex.Vertex(0, 0).name, 1), graph.edges[1])
