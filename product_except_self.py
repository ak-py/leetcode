from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result = [1 for _ in nums]

        for i in range(1, len(nums)):
            result[i] = result[i-1] * nums[i-1]

        temp = 1

        for i in reversed(range(len(nums)-1)):
            temp = temp * nums[i+1]
            result[i] = result[i] * temp

        return result
