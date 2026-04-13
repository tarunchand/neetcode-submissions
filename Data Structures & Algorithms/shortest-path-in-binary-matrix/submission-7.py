from collections import deque

class Solution:
    # Since we know the start and goal nodes - we can use bi-directional BFS which is much more faster
    # since it prevents expanding the last levels of BFS which contains many nodes. All the nodes visited
    # from the start we can track with -1 and all the nodes visited from the bottom - we can track with -2
    # and when we reach a stage when -1 = -2 then we found the solution

    # Bi-directional BFS doesn't work when :-
    # The goal node is unknown
    # The graph is directed without reverse edges
    # The problem has multiple possible goal states
    # State transitions are not reversible

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        q.append((0, 0))
        length = 0
        while q:
            q_len = len(q)
            length +=1
            for _ in range(q_len):
                i, j = q.popleft()
                if i == m or i < 0 or j == n or j < 0:
                    continue
                if grid[i][j] == 1:
                    continue
                if i == m - 1 and j == n - 1:
                    return length
                grid[i][j] = 1
                nodes = [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1), 
                (i + 1, j + 1), (i - 1, j - 1), (i + 1, j - 1), (i - 1, j + 1)]
                for node in nodes:
                    q.append(node)
        return -1