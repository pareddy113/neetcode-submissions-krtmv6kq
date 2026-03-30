class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for(int num: nums) {
            set.add(num);
        }
        int maxLength = 0;
        for(int i = 0; i < nums.length; i++) {
            int count = 1;
            if (!set.contains(nums[i] - count)) {
                while (set.contains(nums[i] + count)) {
                    count++;
                }
                maxLength = Math.max(maxLength, count);
            }
        }
        return maxLength;
    }
}
