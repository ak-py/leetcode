from typing import List

from collections import deque


def is_valid(grid, row, col):
    N = len(grid)
    if row < 0 or row >= N or col < 0 or col >= N or grid[row][col] == 1:
        return False

    return True


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        if not grid or N == 0 or grid[0][0] == 1 or grid[N-1][N-1] == 1:
            return -1

        offsets = [
            (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
        ]

        seen = set()

        start = (0, 0)
        end = (N - 1, N - 1)

        queue = deque()

        queue.append((start, 1))

        while queue:

            (row, col), value = queue.popleft()
            seen.add((row, col))

            if (row, col) == end:
                return value

            for row_off, col_off in offsets:
                if is_valid(grid, row + row_off, col + col_off) and (row + row_off, col + col_off) not in seen:
                    seen.add((row + row_off, col + col_off))
                    queue.append(((row + row_off, col + col_off), value + 1))

        return -1
