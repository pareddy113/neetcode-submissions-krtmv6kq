# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValid(self, root: TreeNode, left: int, right: int) -> bool:
        if not root:
            return True
        if not (left < root.val < right):
            return False
        return self.isValid(root.left, left, root.val) and self.isValid(root.right, root.val, right)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return self.isValid(root, float("-inf"), float("+inf"))        