import collections as collections
import heapq as heapq


# https://gist.github.com/kachayev/5990802
class Dijkstra(object):

    def solve(self, edges, f, t):
        g = collections.defaultdict(list)
        for l, r, c in edges:
            g[l].append((c, r))

        q, seen, mins = [(0, f, ())], set(), {f: 0}
        while q:
            (cost, v1, path) = heapq.heappop(q)
            if v1 not in seen:
                seen.add(v1)
                path = (v1, path)
                if v1 == t:
                    return cost, path

                for c, v2 in g.get(v1, ()):
                    if v2 in seen:
                        continue
                    prev = mins.get(v2, None)
                    next = cost + c
                    if prev is None or next < prev:
                        mins[v2] = next
                        heapq.heappush(q, (next, v2, path))

        return float("inf")
