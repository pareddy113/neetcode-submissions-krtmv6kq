# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        pStack = [(p, q)]

        while pStack:
            pNode, qNode = pStack.pop()
            
            if not pNode and not qNode:
                continue
            if not pNode or not qNode or pNode.val != qNode.val:
                return False;
            
            pStack.append((pNode.left, qNode.left))
            pStack.append((pNode.right, qNode.right))
            
        return True
