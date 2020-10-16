"""

Solved the question without any difficulty within 10 mins. Leetcode tested and submitted it.

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""

Runtime = O(n)
Space = O(n)

"""

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:

        if not root:
            return []

        q = [(root, 0)]
        output = []

        while q:

            node, level = q.pop(0)

            if len(output) != level+1:
                output.append([])

            output[level].append(node.val)

            if node.left:
                q.append((node.left, level + 1))

            if node.right:
                q.append((node.right, level + 1))

        return reversed(output)
