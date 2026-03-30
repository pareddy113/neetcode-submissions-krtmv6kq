class Solution {

    List<List<Integer>> result = new ArrayList<>();
    List<Integer> currentResult = new ArrayList<>();
    
    public void dfs(int[] nums, int index, int target, List<Integer> currResult) {

        if (target == 0) {
            result.add(new ArrayList<>(currResult));
            currResult = new ArrayList<>();
            return;
        }

        if (target < 0) {
            return;
        }

        for (int i = index; i < nums.length; i++) {
            currResult.add(nums[i]);
            dfs(nums, i, target - nums[i], currResult);
            currResult.remove(currResult.size() - 1);
        }
    }

    public List<List<Integer>> combinationSum(int[] nums, int target) {

        for (int i = 0; i < nums.length; i++) {
            currentResult.add(nums[i]);
            dfs(nums, i, target - nums[i], currentResult);
            currentResult.remove(currentResult.size() - 1);
        }
        return result;
    }
}
