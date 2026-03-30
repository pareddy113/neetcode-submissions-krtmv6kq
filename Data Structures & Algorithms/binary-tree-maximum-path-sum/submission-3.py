class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')
        
        def get_max_gain(node):
            nonlocal max_sum
            if not node:
                return 0

            leftSum = get_max_gain(node.left)
            rightSum = get_max_gain(node.right)
            
            maxLeftSum = max(leftSum, 0)
            maxrightSum = max(rightSum, 0)
            
            current_path_sum = node.val + maxLeftSum + maxrightSum
            max_sum = max(max_sum, current_path_sum)
            
            return node.val + max(maxLeftSum, maxrightSum)

        get_max_gain(root)
        return max_sum