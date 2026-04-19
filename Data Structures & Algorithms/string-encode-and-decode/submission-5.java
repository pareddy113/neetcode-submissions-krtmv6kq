class Solution {

    /*
        Encode
         - ["hi", "this", "remembered"]
         2#hi4#this10#remembered

         Decode
            - while(isDigit) find the length
            - substring of the word until the length
    */

    public String encode(List<String> strs) {
        StringBuilder outputString = new StringBuilder();

        for(String str: strs) {
            int length = str.length();
            outputString.append(length);
            outputString.append("#");
            outputString.append(str);
        }
        return outputString.toString();
    }

    public List<String> decode(String str) {
        List<String> output = new ArrayList<>();
        int j = 0;

        while (j < str.length()) {        
            int num = 0;
            while(Character.isDigit(str.charAt(j))){
                num = num * 10 + (str.charAt(j) - '0');
                j++;
            }
            int start = j + 1; // 2
            int end = start + num; // 4
            String word = str.substring(start, end);
            output.add(word);
            j = end;     
        }
        return output;
    }
}
