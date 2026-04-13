from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        visited = set()
        q.append((0, 0))
        visited.add((0, 0))
        length = -1
        while len(q) > 0:
            length += 1
            q_length = len(q)
            for _ in range(q_length):
                i, j = q.popleft()
                if i == m - 1 and j == n - 1:
                    return length 
                for new_i, new_j in [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)]:
                    if new_i >= 0 and new_j >= 0 and new_i < m and new_j < n and grid[new_i][new_j] == 0:
                        if (new_i, new_j) not in visited:
                            visited.add((new_i, new_j))
                            q.append((new_i, new_j))
        return -1
                
            
        