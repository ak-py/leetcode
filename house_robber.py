'''

URL = https://leetcode.com/problems/house-robber/

'''


from typing import List


class Solution:
    # def rob(self, nums: List[int]) -> int:
    #
    #     cache = {}
    #
    #     return self.rob_helper(nums, index=len(nums)-1, cache=cache)
    #
    # def rob_helper(self, nums, index, cache):
    #
    #     if index < 0:
    #         return 0
    #
    #     if index in cache:
    #         return cache[index]
    #
    #     curr = self.rob_helper(nums, index-2, cache) + nums[index]
    #     prev = self.rob_helper(nums, index-1, cache)
    #
    #     result = max(curr, prev)
    #
    #     cache[index] = result
    #
    #     return result

    def rob(self, nums: List[int]) -> int:

        curr, prev = 0, 0

        for num in nums:
            temp = curr
            curr = max(prev + num, curr)
            prev = temp

        return curr
