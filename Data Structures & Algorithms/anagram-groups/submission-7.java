class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {

        //  [strs], group all anagrams into sublists
        // output: any order,

        // sort them, n * m
        // space: O(n)

        Map<String, List<String>> map = new HashMap<>();

        for(String str: strs) {
            char[] charArray = str.toCharArray();
            Arrays.sort(charArray);
            String sortedStr = new String(charArray);
            List<String> value = map.getOrDefault(sortedStr, new ArrayList<String>()); 
            value.add(str);
            map.put(sortedStr, value);
        }
        return new ArrayList<>(map.values());
    }
}
