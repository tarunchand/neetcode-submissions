from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        fresh_fruits_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh_fruits_count += 1
        time = 0
        while q:
            q_len = len(q)
            is_fresh_fruit_available = False
            for _ in range(q_len):
                i, j = q.popleft()
                adj_nodes = [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]
                for next_i, next_j in adj_nodes:
                    if next_i == m or next_i < 0 or next_j == n or next_j < 0:
                        continue
                    if grid[next_i][next_j] != 1:
                        continue
                    grid[next_i][next_j] = 2
                    is_fresh_fruit_available = True
                    fresh_fruits_count -= 1
                    q.append((next_i, next_j))
            if is_fresh_fruit_available:
                time += 1

        return time if fresh_fruits_count == 0 else -1
