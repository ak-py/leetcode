from itertools import product
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        if not board or not board[0]:
            return

        self.ROWS = len(board)
        self.COLS = len(board[0])
        self.board = board

        # get all the edge node
        edges = list(product(range(self.ROWS), [0, self.COLS - 1])) + \
                list(product([0, self.ROWS - 1], range(self.COLS)))

        # mark all the escaped cells
        for row, col in edges:
            self.dfs(row, col)

        # flip the non-escaped Os and put escaped Os back to original state
        for row in range(self.ROWS):
            for col in range(self.COLS):
                if board[row][col] == "E": board[row][col] = "O"
                elif board[row][col] == "O": board[row][col] = "X"

    def dfs(self, row, col):
        if self.board[row][col] != "O":
            return

        self.board[row][col] = "E"

        if row < self.ROWS - 1: self.dfs(row + 1, col)
        if col < self.COLS - 1: self.dfs(row, col + 1)
        if row > 0: self.dfs(row - 1, col)
        if col > 0: self.dfs(row, col - 1)
