import model.vertex as vertex
import model.movement as movement
import model.grid_limit as grid_limit
import algorithm.graph_generator as graph_generator
import algorithm.dijkstra as dijkstra

if __name__ == "__main__":
    start = vertex.Vertex(4, 1)
    end = vertex.Vertex(1, 3)
    movements = [movement.Movement(1, 2), movement.Movement(2, 1),
                 movement.Movement(2, -1), movement.Movement(1, -2),
                 movement.Movement(-1, -2), movement.Movement(-2, -1)]

    limit = grid_limit.GridLimit(0, 5, 0, 3)
    generator = graph_generator.GraphGenerator(movements, limit)
    graph = generator.generate()

    d = dijkstra.Dijkstra()
    solution = d.solve(graph.edges, start.name, end.name)
    # print str(solution[0])
    # print str(solution[1])
    print("Path: ")
    print str(solution[2])

    traversed_nodes = solution[2]
    vertex_map = {}

    for v in graph.vertices:
        vertex_map[v.name] = v

    print("Movements to apply: ")
    for i in range(0, len(traversed_nodes) - 1):
        next_node = vertex_map[traversed_nodes[i + 1]]
        cur_node = vertex_map[traversed_nodes[i]]

        mov_x = next_node.x - cur_node.x
        mov_y = next_node.y - cur_node.y
        print("({}, {})".format(mov_x, mov_y))

    # edges = [
    #     ("A", "B", 7),
    #     ("A", "D", 5),
    #     ("B", "C", 8),
    #     ("B", "D", 9),
    #     ("B", "E", 7),
    #     ("C", "E", 5),
    #     ("D", "E", 15),
    #     ("D", "F", 6),
    #     ("E", "F", 8),
    #     ("E", "G", 9),
    #     ("F", "G", 11)
    # ]
    #
    # d = dijsktra.Dijkstra()
    #
    # print "=== Dijkstra ==="
    # print edges
    # print "A -> E:"
    # print d.solve(edges, "A", "E")
    # print "F -> G:"
    # print d.solve(edges, "F", "G")
