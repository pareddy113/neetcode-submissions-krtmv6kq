class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {

        //  [strs], group all anagrams into sublists
        // output: any order,

        // sort them, n * m
        // space: O(n)

        Map<String, List<String>> map = new HashMap<>();

        for(String str: strs) {
            int[] charArray = new int[26];
            for (char c: str.toCharArray()) {
                charArray[c - 'a']++;
            }
            String key = Arrays.toString(charArray);
            // map.putIfAbsent(key, new ArrayList<>());
            // map.get(key).add(str);
            map.computeIfAbsent(key, k -> new ArrayList<>()).add(str);
        }
        return new ArrayList<>(map.values());
    }
}
