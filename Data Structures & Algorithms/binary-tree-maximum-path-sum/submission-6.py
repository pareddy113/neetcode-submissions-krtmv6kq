class Solution:
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        maxPath=[float("-inf")]

        def maxSum(root):
            if root is None:
                return 0

            leftPath = maxSum(root.left)
            rightPath = maxSum(root.right)

            maxLeftPath = max(leftPath, 0)
            maxRightPath = max(rightPath, 0)

            maxPath[0] = max(maxPath[0], root.val + maxLeftPath + maxRightPath)
            
            return max(root.val + maxLeftPath, root.val + maxRightPath)
        
        maxSum(root)
        return maxPath[0]