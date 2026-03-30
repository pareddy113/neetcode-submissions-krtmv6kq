class Solution {
    /**
    two indices - first & last
    loop (i <= j)
        - (first != last) -> false
        - else
            - continue
    */
    public boolean isPalindrome(String s) {
        int i = 0, j = s.length() - 1;

        if (j < 1) {
            return true;
        }

        while(i <= j) {
            char firstChar = s.charAt(i);
            char lastChar = s.charAt(j);
            if (!Character.isLetterOrDigit(firstChar)) {
                i++;
                continue;
            }
            if (!Character.isLetterOrDigit(lastChar)) {
                j--;
                continue;
            }
            if (Character.toLowerCase(s.charAt(i)) != Character.toLowerCase(s.charAt(j))) {
                return false;
            } 
            i++;
            j--;
        }
        return true;
    }

    public boolean isAlphaNum(char c) {
        return (c >= 'A' && c <= 'Z') 
        || (c >= 'a' && c <= 'z') 
        || (c >= '0' && c <= '9');

    }
}
