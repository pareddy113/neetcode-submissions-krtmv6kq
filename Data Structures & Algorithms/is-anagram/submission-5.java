class Solution {
    public boolean isAnagram(String s, String t) {
        // both strs contain same char
        // lowercase english char

        if (s.length() != t.length()) {
            return false;
        }
        int[] count = new int[26];

        for(int i = 0; i < s.length(); i++) {
            count[s.charAt(i) - 'a']++;
            count[t.charAt(i) - 'a']--;
        }
        return Arrays.stream(count).filter(i -> i != 0).count() == 0;
    }
    
}
