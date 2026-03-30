/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public int kthSmallest(TreeNode root, int k) {

        // BFS - In Order
        if (root == null) {
            return -1;
        }
        int ans = 0;

        ArrayDeque<TreeNode> stack = new ArrayDeque<>();
        
        while (!stack.isEmpty() || root != null) {
            while(root != null) {
                stack.push(root);
                root = root.left;
            }
            TreeNode node = stack.pop();
            k = k - 1;
            if (k == 0){
                ans = node.val;
                break;
            }
            if(node.right != null) {
                stack.push(node.right);
            }
        }
        return ans;
    }
}
