from collections import deque

class Solution:
    def topologicalSort3(self, n: int, edges: List[List[int]]) -> List[int]:
        pre_req_count = [0] * n
        adj_list = dict()
        for i in range(n):
            adj_list[i] = []
        for src, dst in edges:
            adj_list[src].append(dst)
            pre_req_count[dst] += 1
        q = deque()
        for i in range(n):
            if pre_req_count[i] == 0:
                q.append(i)
        res = []
        while q:
            vertex = q.popleft()
            res.append(vertex)
            for next_vertex in adj_list.get(vertex, []):
                pre_req_count[next_vertex] -= 1
                if pre_req_count[next_vertex] == 0:
                    q.append(next_vertex)
        # Detecting loops
        return res if len(res) == n else []

    def topologicalSort2(self, n: int, edges: List[List[int]]) -> List[int]:
        pre_req_count = [0] * n
        adj_list = dict()
        for i in range(n):
            adj_list[i] = []
        for src, dst in edges:
            adj_list[src].append(dst)
            pre_req_count[dst] += 1

        def dfs(i):
            if pre_req_count[i] != 0:
                return
            pre_req_count[i] = -1
            res.append(i)
            for next_i in adj_list.get(i, []):
                pre_req_count[next_i] -= 1
                dfs(next_i)

        res = []
        for i in range(n):
            dfs(i)
        return res if len(res) == n else []

    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        # Reverse the edges of the graph and run a post-order traversal (Visit leaves first and then root).
        # or Run Post-Order Traversal and reverse the answer. Why it works :- because in post order we are
        # visiting children and their children first before visiting parents so the grand children comes
        # first in the output and the grand parent comes last in the output and if you reverse it then
        # grand parent comes first in the output and grand children comes last in the output.
        adj_list = dict()
        for i in range(n):
            adj_list[i] = []
        for src, dst in edges:
            adj_list[src].append(dst)

        visited = set()
        res = []

        def dfs(i, cycle_detection):
            if i in cycle_detection:
                return False
            if i in visited:
                return True
            visited.add(i)
            cycle_detection.add(i)
            result = True
            for next_i in adj_list.get(i, []):
                result = result and dfs(next_i, cycle_detection)
            res.append(i)
            cycle_detection.remove(i)
            return result
        
        for i in range(n):
            if not dfs(i, set()):
                return []

        return res[::-1]
