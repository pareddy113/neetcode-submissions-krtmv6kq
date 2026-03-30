# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        stack = [[root, -float('inf')]]
        res = 0
        while stack:
            node, currentMax = stack.pop()
            if node.val >= currentMax:
                res += 1
            currentMax = max(currentMax, node.val)

            if node.left:
                stack.append([node.left, currentMax])
            if node.right:
                stack.append([node.right, currentMax])
            
        return res    