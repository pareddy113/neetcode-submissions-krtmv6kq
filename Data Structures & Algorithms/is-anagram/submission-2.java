class Solution {
    public boolean isAnagram(String s, String t) {

        int[] scharCountMap = new int[26];

        if (s.length() != t.length()) {
            return false;
        }

        for(int i = 0; i < s.length(); i++) {
            scharCountMap[s.charAt(i) - 'a'] = scharCountMap[s.charAt(i) - 'a'] + 1;
            scharCountMap[t.charAt(i) - 'a'] = scharCountMap[t.charAt(i) - 'a'] - 1;
        }
    
        for(int i = 0; i < scharCountMap.length; i++) {
            if (scharCountMap[i] > 0) {
                return false;
            }        
        }
        return true;
        
    }
}
