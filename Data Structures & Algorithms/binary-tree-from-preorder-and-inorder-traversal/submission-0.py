# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Binary tree
        # preorder [1,2,3,4]
        # inorder [2,1,3,4]
        node = None
        
        map = { val: index for index, val in enumerate(inorder) }

        self.pre_idx = 0
        def tree(i, j):

            if (i > j):
                return None
            
            rootVal = preorder[self.pre_idx]
            self.pre_idx += 1
            index = map[rootVal]
            root = TreeNode(rootVal)
            root.left = tree(i, index -1)
            root.right = tree(index + 1, j)
            return root
    
        return tree(0, len(preorder) - 1)



