from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        sums = defaultdict(int)
        sums[0] = 1
        subtotal = 0
        result = 0

        for val in nums:
            subtotal += val
            if (subtotal - k) in sums:
                result += sums[subtotal-k]
            sums[subtotal] += 1

        return result
