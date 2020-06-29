from typing import List


class Solution:
    def trap_old(self, height: List[int]) -> int:
        length = len(height)
        if not height or length <= 2:
            return 0

        l_max = [0 for _ in height]
        l_max[0] = height[0]

        r_max = [0 for _ in height]
        r_max[length - 1] = height[length - 1]

        for i in range(1, length):
            l_max[i] = max(l_max[i - 1], height[i])

        for i in range(length - 2, -1, -1):
            r_max[i] = max(r_max[i + 1], height[i])

        total = 0

        for i in range(length):
            height_delta = min(l_max[i], r_max[i])
            curr = height[i]
            if height_delta - curr > 0:
                total += height_delta - curr

        return total

    def trap(self, heights):

        N = len(heights)

        l, r = 0, N - 1
        lmax, rmax = 0

        total = 0

        while l < r:
            if heights[l] < heights[r]:
                if heights[l] >= lmax:
                    lmax = heights[l]
                else:
                    total += lmax - heights[l]
                l += 1
            else:
                if heights[r] >= rmax:
                    rmax = heights[r]
                else:
                    total += rmax - heights[r]
                r -= 1

        return total
