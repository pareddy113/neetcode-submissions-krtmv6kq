class Solution {
    public int lengthOfLongestSubstring(String s) {
        
        HashMap<Character, Integer> map = new HashMap<>();
        int longestSubStrLength = 0;

        for(int left = 0, right = 0; right < s.length(); right++) {
            Character ch = s.charAt(right);
            map.put(ch, map.getOrDefault(ch, 0) + 1 );
            while(map.get(ch) > 1) {
                Character leftCh = s.charAt(left);
                map.put(leftCh, map.getOrDefault(leftCh, 0) - 1 );
                left++;
            }
            longestSubStrLength = Math.max(longestSubStrLength, right - left + 1);
        }
        return longestSubStrLength;
    }
}
