"""

URL - https://leetcode.com/problems/generate-parentheses/

REDO - long term

"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        self.result = []
        self.dfs(n, n, [])
        return self.result

    def dfs(self, left_remain, right_remain, temp):

        # base case
        if left_remain == 0 and right_remain == 0:
            temp_string = "".join(temp)
            self.result.append(temp_string)
            return

        # add left bracket
        if left_remain > 0:
            temp.append("(")
            self.dfs(left_remain-1, right_remain, temp)
            temp.pop()

        # add right bracket
        if right_remain > 0 and right_remain > left_remain:
            temp.append(")")
            self.dfs(left_remain, right_remain-1, temp)
            temp.pop()


sol = Solution()
print(sol.generateParenthesis(0))
