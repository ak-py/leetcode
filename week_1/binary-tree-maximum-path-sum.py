"""

Had the correct idea on paper. Hard time coding it up in recursion.

Ended up with many missed edge cases. Need to test more.

Looked at the solution. Realized the simpler way.

Coded it up.

took total of 45 mins

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.res = -1000
        self.helper(root)
        return self.res

    def helper(self, node):

        if not node:
            return 0

        left_gain = max(self.helper(node.left), 0)
        right_gain = max(self.helper(node.right), 0)

        center_path = node.val + left_gain + right_gain
        self.res = max(self.res, center_path)

        return node.val + max(left_gain, right_gain)