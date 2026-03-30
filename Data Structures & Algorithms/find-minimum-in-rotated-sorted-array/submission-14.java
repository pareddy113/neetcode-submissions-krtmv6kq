class Solution {
    public int findMin(int[] nums) {
        int start = 0, end = nums.length - 1;
        int min = Integer.MAX_VALUE;
        while (start <= end) {
            int mid = start + (end - start) / 2;
            min = Math.min(min, nums[mid]);
            // If mid element is greater than end, min is in the right half
            if (nums[mid] > nums[end]) {
                start = mid + 1;
            } else {
                // mid could be the min, so include it
                end = mid - 1;
            }
        }

        return min;
    }
}
