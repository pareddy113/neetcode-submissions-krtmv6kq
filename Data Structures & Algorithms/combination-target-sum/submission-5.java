class Solution {
    public List<List<Integer>> combinationSum(int[] nums, int target) {
        
        List<List<Integer>> ans = new ArrayList<>();
        backtrack(nums, 0, new ArrayList(), ans, target);
        return ans;
    }

    private void backtrack(int[] nums, int index, List<Integer> subset, List<List<Integer>> output, int target) {

        if (target == 0) {
            output.add(new ArrayList<>(subset));
        }

        if (target < 0) {
            return;
        }

        for(int i = index; i < nums.length; i++) {
            subset.add(nums[i]);
            backtrack(nums, i, subset, output, target - nums[i]);
            subset.removeLast();
        }

    }
}
