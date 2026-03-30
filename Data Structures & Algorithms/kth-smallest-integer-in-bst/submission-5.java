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

        List<Integer> arr = new ArrayList<>();
        ArrayDeque<TreeNode> stack = new ArrayDeque<>();
        
        while (!stack.isEmpty() || root != null) {
            while(root != null) {
                stack.push(root);
                root = root.left;
            }
            TreeNode node = stack.pop();
            // k = k - 1;
            arr.add(node.val);
            if (node.right != null) {
                stack.push(node.right);
            }
        }
        System.out.println(arr);
        return arr.get(k-1);
    }
}
