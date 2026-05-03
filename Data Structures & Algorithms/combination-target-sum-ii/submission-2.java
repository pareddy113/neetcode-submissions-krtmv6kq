class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        List<List<Integer>> ans = new ArrayList<>();
        Arrays.sort(candidates);
        backtrack(candidates, 0, new ArrayList(), ans, target);
        return ans;
    }

    // 1 2 2 4 5 6 9
    private void backtrack(int[] nums, int index, List<Integer> subset, List<List<Integer>> output, int target) {

        if (target == 0) {
            output.add(new ArrayList<>(subset));
            return;
        }

        if (target < 0) {
            return;
        }

        for(int i = index; i < nums.length; i++) {
            if (i > index && nums[i] == nums[i-1]) {
                continue;
            }            
            
            subset.add(nums[i]);
            backtrack(nums, i + 1, subset, output, target - nums[i]);
            subset.removeLast();
        }

    }
}
