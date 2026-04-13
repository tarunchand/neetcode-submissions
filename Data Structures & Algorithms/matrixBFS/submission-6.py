from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visit = set()
        queue = deque()
        queue.append((0, 0))
        visit.add((0, 0))

        length = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == m - 1 and c == n - 1:
                    return length

                neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in neighbors:
                    if (min(r + dr, c + dc) < 0 or
                        r + dr == m or c + dc == n or
                        (r + dr, c + dc) in visit or grid[r + dr][c + dc] == 1):
                        continue
                    queue.append((r + dr, c + dc))
                    visit.add((r + dr, c + dc))
            length += 1
        return -1

    def shortestPath2(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque()
        queue.append((0, 0))
        length = -1

        while queue:
            length += 1
            q_length = len(q)
            for _ in range(q_length):
                i, j = queue.popleft()
                if i == m - 1 and j == n - 1:
                    return length
                if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 1:
                    continue
                grid[i][j] = 1
                for new_i, new_j in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    queue.append((new_i, new_j))

        return -1


        return -1