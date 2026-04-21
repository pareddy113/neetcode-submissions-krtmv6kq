class Solution {
    /*
        given nums[]
        return all triplets[i,j,k] no duplicates, any order

        O(n^3)

        O(n logn) + O(n^2)

        O(1)

        [-4,-1,-1,0,1,2]
    */
    public List<List<Integer>> threeSum(int[] nums) {
        
        Arrays.sort(nums);
        List<List<Integer>> output = new ArrayList<>();

        for (int i = 0; i < nums.length; i++) {
            if (i > 0 && (nums[i] == nums[i-1])) {
                continue;
            }

            int l = i + 1;
            int r = nums.length - 1;

            while (l < r) {
                if (nums[l] + nums[r] + nums[i] < 0) {
                    l++;
                } else if (nums[l] + nums[r] + nums[i] > 0) {
                    r--;
                } else {
                    output.add(Arrays.asList(nums[i], nums[l], nums[r]));
                    System.out.println(nums[i] + " " + nums[l] + " " + nums[r]);
                    l++;
                    r--;
                    while(l < r && nums[l] == nums[l - 1]) {
                        l++;
                    }
                }
            }
        }
        return output;
    }
}
