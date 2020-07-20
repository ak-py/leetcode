import collections
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        if k >= len(nums):
            return nums

        counts = collections.Counter(nums)

        return heapq.nlargest(k, counts.keys(), key=counts.get)

