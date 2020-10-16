# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        def bfs(node):
            if not node:
                return 0

            deq = deque()
            max_zigzag_size = 0

            if root.left:
                deq.append((node.left, 'l', 1))
            if root.right:
                deq.append((node.right, 'r', 1))

            while deq:
                node, from_, zigzag_size = deq.popleft()
                max_zigzag_size = max(zigzag_size, max_zigzag_size)  # update max len of zigzag path

                if node.left:
                    if from_ == 'l':
                        deq.append((node.left, "l", 1))  # reset length
                    if from_ == 'r':  # if came from right
                        deq.append((node.left, "l", zigzag_size + 1))  # increase length

                if node.right:
                    if from_ == 'l':
                        deq.append((node.right, "r", zigzag_size + 1))  # increase length
                    if from_ == 'r':
                        deq.append((node.right, "r", 1))  # reset length
            return max_zigzag_size

        return bfs(root)


