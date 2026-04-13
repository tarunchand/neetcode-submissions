from collections import deque

class Solution:
    def topologicalSort2(self, n: int, edges: List[List[int]]) -> List[int]:
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
        return res if len(res) == n else []

    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        pre_req_count = [0] * n
        adj_list = dict()
        for i in range(n):
            adj_list[i] = []
        for src, dst in edges:
            adj_list[src].append(dst)
            pre_req_count[dst] += 1
        q = deque()

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
        