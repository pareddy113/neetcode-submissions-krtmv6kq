class Solution {
    public boolean canJump(int[] nums) {
        
        Integer maxJump = 0;

        /*
            1,3         
        */
        for(int i = 0; i < nums.length; i++) {
            maxJump = Math.max(maxJump, i + nums[i]);

            if (maxJump == nums.length - 1) {
                return true;
            }

            if (i >= maxJump) {
                return false;
            }
        }
        return true;
    }
}
