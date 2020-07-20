from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        result = []

        nums.sort()

        for i, val in enumerate(nums):
            target = -val

            left = i
            right = len(nums)-1

            while left < right:

                total = nums[left] + nums[right]

                if total > target:
                    right -= 1
                    pass
                elif total < target:
                    left += 1
                else:
                    result.append([val, nums[left], nums[right]])
                    break

        return result
