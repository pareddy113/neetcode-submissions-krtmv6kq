class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> duplicateSet = new HashSet<Integer>();
        for (Integer num: nums) {
            if (duplicateSet.contains(num)) {
                return true;
            }
            duplicateSet.add(num);
        }
        return false;
    }
}