from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        sums = {}

        total = 0

        req_len = 2

        for index, val in enumerate(nums):
            total += val

            if k != 0:
                total = total % k

            if total in sums:
                if index - sums[total] >= req_len:
                    return True

            else:
                sums[total] = index

        return False
