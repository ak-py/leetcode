from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        n = len(board)
        m = len(board[0])
        if len(word) > (m * n): return False

        for row in range(n):
            for col in range(m):
                if board[row][col] == word[0]:
                    found = self.search(board, row, col, word)
                    if found:
                        return True

        return False

    def search(self, board, row, col, word, seen=None):

        if seen is None: seen = set()

        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or (row, col) in seen:
            return False

        if board[row][col] == word[0]:
            seen.add((row, col))

            if len(word) == 1:
                return True

            up = self.search(board, row - 1, col, word[1::], seen)
            down = self.search(board, row + 1, col, word[1::], seen)
            left = self.search(board, row, col - 1, word[1::], seen)
            right = self.search(board, row, col + 1, word[1::], seen)

            return up or down or left or right
        return False
