class Solution {
    public int lengthOfLongestSubstring(String s) {
        
        Set<Character> hashSet = new HashSet<>();
        int longestSubStrLength = 0;

        for(int left = 0, right = 0; right < s.length(); right++) {
            Character ch = s.charAt(right);
            
            while(hashSet.contains(ch)) {
                hashSet.remove(s.charAt(left));
                left++;
            }
            hashSet.add(s.charAt(right));
            longestSubStrLength = Math.max(longestSubStrLength, right - left + 1);
        }
        return longestSubStrLength;
    }
}
