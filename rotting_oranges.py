from typing import List


def is_in_bounds(grid, row, col):
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])


def extract_fresh_and_rotten(grid):
    fresh = 0
    queue = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 2:
                queue.append(((row, col), 0))
            elif grid[row][col] == 1:
                fresh += 1
    return queue, fresh


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        queue, fresh = extract_fresh_and_rotten(grid)

        offsets = [(0, -1), (-1, 0), (0, 1), (1, 0)]

        max_time = 0

        while queue:

            (row, col), time = queue.pop(0)

            for row_off, col_off in offsets:
                new_row, new_col = row + row_off, col + col_off
                if is_in_bounds(grid, new_row, new_col) and grid[new_row][new_col] == 1:
                    grid[new_row][new_col] = 2
                    fresh -= 1
                    max_time = max(max_time, time+1)
                    queue.append(((new_row, new_col), time+1))

        return max_time if fresh == 0 else -1
