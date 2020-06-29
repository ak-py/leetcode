class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        ROWS = len(matrix)
        COLS = len(matrix[0])

        row = ROWS - 1
        col = 0

        while row >= 0 and col < COLS:

            cell = matrix[row][col]

            if cell == target:
                return True

            elif cell > target:
                row -= 1
            else:
                col += 1
        return False
