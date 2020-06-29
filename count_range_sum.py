from typing import List


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        self.lower = lower
        self.upper = upper

        self.valid_ranges = set()

        n = len(nums)

        left = [0 for _ in nums]
        right = [0 for _ in nums]

        for i in range(n):
            prev = left[i - 1] if i > 0 else 0
            left[i] = prev + nums[i]
            if self.is_in_range(left[i]):
                self.valid_ranges.add((0, ))

        pass

    def is_in_range(self, value):
        return value >= self.lower and value <= self.upper
