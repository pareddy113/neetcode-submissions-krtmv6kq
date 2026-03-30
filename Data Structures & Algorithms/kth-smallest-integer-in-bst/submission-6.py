# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        if not root:
            return 0

        stack = []
        current = root

        # 3
        # 1  k=0 
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            
            current = stack.pop()

            if k == 1:
                return current.val
            
            k = k - 1
            current = current.right
        