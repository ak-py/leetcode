
'''

URL = https://leetcode.com/problems/house-robber-ii/

'''


from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums)

        use_first = self.rob_helper(nums[:-1], index=len(nums)-2, cache={})
        use_last = self.rob_helper(nums[1:], index=len(nums)-2, cache={})

        return max(use_first, use_last)

    def rob_helper(self, nums, index, cache):

        if index < 0:
            return 0

        if index in cache:
            return cache[index]

        curr = self.rob_helper(nums, index-2, cache) + nums[index]
        prev = self.rob_helper(nums, index-1, cache)

        result = max(curr, prev)

        cache[index] = result

        return result
