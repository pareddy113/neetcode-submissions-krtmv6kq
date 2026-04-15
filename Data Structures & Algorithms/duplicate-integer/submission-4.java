class Solution {
    public boolean hasDuplicate(int[] nums) {
        
        // nums [] -> true if freq(x) > 1
        
        HashSet<Integer> freq = new HashSet<>();
        for(int num: nums) {
            if (freq.contains(num)) {
                return true;
            }
            freq.add(num);
        }
        return false;
    }
}