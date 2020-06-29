class Solution:
    def searchMatrix(self, matrix, target):
        # initial_list = []
        # single_list = [initial_list.extend(i) for i in matrix]

        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        M = len(matrix)
        N = len(matrix[0])

        high = M * N - 1
        low = 0

        while low <= high:
            mid = (high + low) // 2
            row, col = calc_index(mid, N)
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                high = mid - 1
            else:
                low = mid + 1

        return False


def calc_index(abs_index, N):
    return abs_index // N, abs_index % N