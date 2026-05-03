class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> ans = new ArrayList<>();
        backtrack(nums, 0, new ArrayList(), ans);
        return ans;
    }

    private void backtrack(int[] nums, int index, List<Integer> subset, List<List<Integer>> output) {

        output.add(new ArrayList<>(subset));

        for(int i = index; i < nums.length; i++) {
            subset.add(nums[i]);
            backtrack(nums, i + 1, subset, output);
            subset.removeLast();
        }

    }
}
