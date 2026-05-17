class Solution {
    public int maxSubArray(int[] nums) {

    /*
        max = -inf,
        [2,-3,4,-2,2,1,-1,4]
        2
    */
     Integer maxSum = Integer.MIN_VALUE;
     Integer currSum = 0;
     
     for( int num: nums) {
        if (currSum < 0) {
            currSum = 0;
        }
        currSum += num;
        maxSum = Math.max(maxSum, currSum);
     }

     return maxSum;

    }
}
