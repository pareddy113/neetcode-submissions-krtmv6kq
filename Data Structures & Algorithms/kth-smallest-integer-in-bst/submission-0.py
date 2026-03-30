# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = []
        self.small(root, ans)
        return ans[k-1]

    def small(self, root, ans):
        if not root:
            return None

        if root.left:
            self.small(root.left, ans)
        ans.append(root.val)
        if root.right:
            self.small(root.right, ans)
    

