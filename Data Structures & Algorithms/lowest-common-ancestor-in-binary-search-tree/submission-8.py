# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        # BST - Lowest common ancestor

        # p < root < q -> answer

        # root > both values -> lowestCommonAncestor(root.left)
        # root < both values -> lowestCommonAncestor(root.right)
        if not root or not p or not q:
            return None

        if min(p.val, q.val) > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif max(p.val, q.val) < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root
