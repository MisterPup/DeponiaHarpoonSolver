import model.vertex as vertex
import model.movement as movement
import model.grid_limit as grid_limit
import algorithm.graph_generator as graph_generator
import algorithm.dijsktra as dijsktra


if __name__ == "__main__":
    start = vertex.Vertex(4, 1)
    end = vertex.Vertex(1, 3)
    movements = [movement.Movement(1, 2), movement.Movement(2, 1),
                 movement.Movement(2, -1), movement.Movement(1, -2),
                 movement.Movement(-1, -2), movement.Movement(-2, -1)]

    limit = grid_limit.GridLimit(0, 5, 0, 3)
    generator = graph_generator.GraphGenerator(movements, limit)
    graph = generator.generate()

    d = dijsktra.Dijkstra()
    solution = d.solve(graph.edges, start.name, end.name)
    print str(solution)
