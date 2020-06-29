# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.big = None     # 3
        self.small = None   # 2
        self.prev = None    # 4

        self.in_order(root)
        self.swap()

    def in_order(self, node):   # [(3), 1, 4, 2]

        if not node:
            return

        self.in_order(node.left)

        if self.prev and self.prev.val > node.val:
            self.small = node
            if self.big is None:
                self.big = self.prev
            else:
                return

        self.prev = node

        self.in_order(node.right)

    def swap(self):
        # interchange self.big and self.small
        self.big.val, self.small.val = self.small.val, self.big.val
