"""

URL - https://leetcode.com/problems/subsets/

REDO - long term

"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        if not nums:
            return [[]]
        self.nums = nums
        self.result = []
        self.dfs(0, 0, [])

        return self.result

    def dfs(self, index, level, temp):

        # base case
        if level == len(self.nums):
            self.result.append(temp[:])
            return

        # recursive cases

        # add new index
        temp.append(self.nums[index])
        self.dfs(index + 1, level + 1, temp)

        # add nothing
        temp.pop()
        self.dfs(index + 1, level + 1, temp)


sol = Solution()
print(sol.subsets(["a", "b", "c"]))
