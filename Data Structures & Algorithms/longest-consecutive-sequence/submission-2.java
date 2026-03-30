class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for(int num: nums) {
            set.add(num);
        }
        int maxLength = 0;
        System.out.println(Arrays.toString(nums));
        for(int i = 0; i < nums.length; i++) {
            int count = 1;
            while (set.contains(nums[i] - count)) {
                System.out.println(nums[i] + " " + count);
                count++;
            }
            maxLength = Math.max(maxLength, count);
        }
        return maxLength;
    }
}
