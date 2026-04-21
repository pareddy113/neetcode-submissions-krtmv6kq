class Solution {

    /*
        given nums
        longest consecutive sequence

        TC - O(n)

    */
    public int longestConsecutive(int[] nums) {
        
        Set<Integer> set = new HashSet<>();

        if (nums.length == 0) {
            return 0;
        }

        for (int num: nums) {
            set.add(num);
        }
        int max_count = 0;
        for (int i = 0; i < nums.length; i++) {

            if (set.contains(nums[i] - 1)) {
                continue;
            }
            int k = 1;
            while (set.contains(nums[i] + k)) {
                k++;
            }
            max_count = Math.max(max_count, k);
        }
        return max_count;
    }
}
