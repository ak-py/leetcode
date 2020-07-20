import heapq
from typing import List


class Pointer:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self):
        return self.x ** 2 + self.y ** 2

    def __lt__(self, other):
        return self.dist() < other.dist()


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

        heap = []

        for x, y in points:
            heapq.heappush(heap, Pointer(x, y))

            if len(heap) > K:
                heapq.heappop(heap)

        result = []

        for _ in range(K):
            pt = heapq.heappop(heap)
            result.append([pt.x, pt.y])

        result.reverse()

        return result
