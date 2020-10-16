from collections import defaultdict


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""

Runtime = O(N)
Space = O(N/2) - max width of the last level in complete tree

"""



# class Solution:
#     def deepestLeavesSum(self, root: TreeNode) -> int:
#
#         if not root:
#             return 0
#
#         q = [(root, 0)]
#         max_depth = 0
#         max_depth_sum = 0
#
#         while q:
#
#             node, level = q.pop(0)
#             if not node:
#                 continue
#             if level > max_depth:
#                 max_depth = level
#                 max_depth_sum = node.val
#             elif level == max_depth:
#                 max_depth_sum += node.val
#
#             if node.left:
#                 q.append((node.left, level + 1))
#
#             if node.right:
#                 q.append((node.right, level + 1))
#
#         return max_depth_sum

"""

Runtime = O(N)
Space = O(H) = height of the tree - balanced tree has height log(n) 

"""


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:

        if not root:
            return 0

        q = [(root, 0)]
        max_depth = 0
        max_depth_sum = 0

        while q:

            node, level = q.pop()
            if not node:
                continue

            if level > max_depth:
                max_depth = level
                max_depth_sum = node.val
            elif level == max_depth:
                max_depth_sum += node.val

            if node.right:
                q.append((node.right, level + 1))

            if node.left:
                q.append((node.left, level + 1))

        return max_depth_sum
