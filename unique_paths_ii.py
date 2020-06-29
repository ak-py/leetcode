from typing import List


"""
Leetcode

63. Unique Paths II

https://leetcode.com/problems/unique-paths-ii/

Runtime - O( n x m )
Space - O (n x m )


Follow up - What if you can change the original grid - can you do it in O(1) space?

"""

class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        self.grid = grid
        self.ROWS = len(grid)
        self.COLS = len(grid[0])

        value = self.dfs()

        return value

    def dfs(self, row=0, col=0, memo=None):

        if memo is None:
            memo = {(self.ROWS - 1, self.COLS - 1): 1}

        if row >= self.ROWS or col >= self.COLS or self.grid[row][col] == 1:
            memo[(row, col)] = 0
            return 0

        if (row, col) not in memo:
            right = self.dfs(row, col+1, memo)
            down = self.dfs(row+1, col, memo)
            memo[(row, col)] = right + down

        return memo[(row, col)]
