import collections as collections
import heapq as heapq


# https://gist.github.com/kachayev/5990802
# https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm#Using_a_priority_queue
class Dijkstra(object):

    """
    edges = [(node1, node2, cost)]
    f = start_node
    t = end_node
    """
    def solve(self, edges, f, t):
        g = collections.defaultdict(list)  # g[k] = [] if key is missing
        for l, r, c in edges:
            g[l].append((c, r))  # g[l] = list of neighbors r of l with costs c

        q, seen, mins = [(0, f, (), [])], set(), {f: 0}
        # q = list of (cost of path to v, vertex v, path to v)
        # seen = list of seen nodes
        # mins = cost of path from f to node k for each k

        while q:
            (cost, v1, path, traversed_nodes) = heapq.heappop(q)  # Pop and return the vertex with current smallest cost
            if v1 not in seen:
                seen.add(v1)
                path = (v1, path)
                traversed_nodes.append(v1)
                if v1 == t:
                    return cost, path, traversed_nodes

                for c, v2 in g.get(v1, ()):  # list of neighbours v2 of v1 and their current cost
                    if v2 in seen:
                        continue
                    prev = mins.get(v2, None)  # get cost of path to v2
                    next = cost + c
                    if prev is None or next < prev:
                        mins[v2] = next
                        heapq.heappush(q, (next, v2, path, list(traversed_nodes)))

        return float("inf")
