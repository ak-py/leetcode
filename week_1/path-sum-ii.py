# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:

        if not root:
            return []

        q = [(root, root.val, [root.val])]

        output = []

        while q:

            node, total, seq = q.pop() # 8, 13, [5, 8]

            if not node.left and not node.right:
                if total == target:
                    output.append(seq)
                continue

            if node.left:
                left_val = node.left.val
                q.append((node.left, total + left_val, seq+[left_val]))

            if node.right:
                right_val = node.right.val
                q.append((node.right, total + right_val, seq+[right_val]))

        return output
