import heapq

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj_list = dict()
        for i in range(n):
            adj_list[i] = []
        for src, dst, weight in edges:
            adj_list[src].append((dst, weight))
            adj_list[dst].append((src, weight))
        total_weight = 0
        visited = set()
        heap = [(0, 0)]
        while heap and len(visited) < n:
            print(heap)
            distance, vertex = heapq.heappop(heap)
            if vertex in visited:
                continue
            visited.add(vertex)
            total_weight += distance
            for dst, weight in adj_list.get(vertex, []):
                heapq.heappush(heap, (weight, dst))
            
        return total_weight if len(visited) == n else -1
