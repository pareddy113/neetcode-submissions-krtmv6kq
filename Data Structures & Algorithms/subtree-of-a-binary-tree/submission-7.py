# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.isSubtreeMethod(root, subRoot, False)
        
    def isSubtreeMethod(self, root: Optional[TreeNode], subRoot: Optional[TreeNode], found) -> bool:
        if not root and not subRoot:
            return True

        if not root or not subRoot:
            return False

        if (root.val == subRoot.val):
            print(root.val)
            found = found or self.sameTrees(root, subRoot) or self.isSubtreeMethod(root.left, subRoot, found) or self.isSubtreeMethod(root.right, subRoot, found)
        else:
            found = found or self.isSubtreeMethod(root.left, subRoot, found) or self.isSubtreeMethod(root.right, subRoot, found)
        return found
        

    def sameTrees(self, root, subRoot):
        if not root and not subRoot:
            return True
            
        if not root or not subRoot or root.val != subRoot.val:
            return False
        
        return self.sameTrees(root.left, subRoot.left) and self.sameTrees(root.right, subRoot.right)

        