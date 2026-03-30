# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [[1, root]]
        res = 0
        while stack:
            current = stack.pop()
            height = current[0]
            node = current[1]
            res = max(res, height)
            if node.left:
                stack.append([height + 1, node.left])
            if node.right:
                stack.append([height + 1, node.right])
        return res

        