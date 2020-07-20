'''

URL = https://leetcode.com/problems/house-robber-iii/

'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: TreeNode) -> int:

        result = self.rob_helper(root, cache={})

        return result

    def rob_helper(self, node, cache) -> int:

        if not node:
            return 0

        if node in cache:
            return cache[node]

        result = 0

        if node.left:
            result += self.rob_helper(node.left.left, cache) + self.rob_helper(node.left.right, cache)

        if node.right:
            result += self.rob_helper(node.right.left, cache) + self.rob_helper(node.right.right, cache)

        result = max(result + node.val, self.rob_helper(node.left, cache) + self.rob_helper(node.right, cache))

        cache[node] = result

        return result
