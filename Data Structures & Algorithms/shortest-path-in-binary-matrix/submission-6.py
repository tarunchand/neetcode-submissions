from collections import deque

class Solution:
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