import heapq

class Path:

    def __init__(self, vertex, distance):
        self.vertex = vertex
        self.distance = distance

    def __lt__(self, other):
        return self.distance < other.distance

    def __eq__(self, other):
        return self.vertex == other.vertex and self.distance == other.distance

    def __gt__(self, other):
        return self.distance > other.distance

    def __repr__(self):
        return "Path(Vertex = {}, Distance = {})".format(self.vertex, self.distance)


class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src_vertex: int) -> Dict[int, int]:
        adj = dict()
        for src, dst, weight in edges:
            if src in adj:
                adj[src].append((dst, weight))
            else:
                adj[src] = [(dst, weight)]

        res = dict()
        for i in range(n):
            res[i] = -1

        heap = [Path(src_vertex, 0)]
        while heap:
            print(heap)
            cur_vertex = heapq.heappop(heap)
            cur_shortest_distance = res.get(cur_vertex.vertex, -1)
            if cur_shortest_distance != -1 and cur_shortest_distance <= cur_vertex.distance:
                continue
            res[cur_vertex.vertex] = cur_vertex.distance
            for dst, weight in adj.get(cur_vertex.vertex, []):
                heapq.heappush(heap, Path(dst, weight + cur_vertex.distance))

        return res
            
