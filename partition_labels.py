'''

Took me about 30 mins to fully code the solution and get run my test cases. Was successful on leetcode in the first try.
Looked at the solutions to see if I could write it cleaner.

'''

from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:

        if not S:
            return [0]

        if len(S) == 1:
            return [1]

        last_seen = {}
        for index, value in enumerate(S):
            last_seen[value] = index

        results = []

        start = end = 0

        for index, value in enumerate(S):
            end = max(last_seen[value], end)

            if index == end:
                results.append(index - start + 1)
                start = index + 1

        return results


test_1 = "xxxy"
test_2 = "xyz"
test_3 = "a"
test_4 = "abcaefeghij"
sol = Solution()
print(sol.partitionLabels(test_1))
print(sol.partitionLabels(test_2))
print(sol.partitionLabels(test_3))
print(sol.partitionLabels(test_4))
