class Solution {
    public int[] productExceptSelf(int[] nums) {
        /*
            [1,2,4,6]
            [1,1,2,8]
            [48,24,6,1]

            [48, 24, 12, 8]

        */
        int length = nums.length;
        int[] output = new int[length];
        int[] prefix = new int[length];
        int[] suffix = new int[length];

        prefix[0] = 1;
        suffix[length - 1 ] = 1;

        for (int i = 1; i < length; i++) {
            prefix[i] = prefix[i - 1] * nums[i - 1];
        }

        for (int i = length - 2; i >= 0; i--) {
            suffix[i] = suffix[i + 1] * nums[i + 1];
        }

        for (int i = 0; i < length; i++) {
            output[i] = suffix[i] * prefix[i];
        }
        return output;
    }
}  
