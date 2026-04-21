class Solution {
    public boolean isPalindrome(String s) {

        int l = 0;
        int r = s.length() - 1;

        while (l <= r) {
            char leftChar = s.charAt(l);
            if (!isAlphaNumeric(leftChar)) {
                l++;
                continue;
            }
            int c = leftChar;
  
            char rightChar = s.charAt(r);
            if (!isAlphaNumeric(rightChar)) {
                r--;
                continue;
            }

            if (Character.toLowerCase(s.charAt(l)) != Character.toLowerCase(s.charAt(r))){
                return false;
            }

            l++;
            r--;
        }
        return true;
    }

    private boolean isAlphaNumeric(char c) {
        return (c >='a' && c <= 'z') || (c >='A' && c<= 'Z') || (c>='0' && c<= '9');
    }
}
