class Solution {
    public int[] twoSum(int[] nums, int target) {
        // nums
        // target = nums[i] + nums[j] i!=j
        // return small index first
        //  exactly one pair

        // map={val:index}
        // [3,4,5,6] 7

        Map<Integer, Integer> map = new HashMap<>();
        int[] ans = new int[2];
        for(int i = 0; i < nums.length; i++) {
            int reqValue = target - nums[i];
            if (map.containsKey(reqValue)) {
                int smallIndex = map.get(reqValue);
                return new int[]{smallIndex, i};
            }
            map.put(nums[i], i);
        }
        return new int[]{-1,-1};
    }
}
