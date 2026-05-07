class Solution {
    /*

        n - 0 ""
        n - 1   ( )
        n - 2  ( ) ( )
        n - 3 () () () ()
    */
    public List<String> generateParenthesis(int n) {
        List<String> output = new ArrayList<>();
        StringBuilder str = new StringBuilder();
        backtrack(output, str, n, 0, 0);
        return output;
    }

    private void backtrack(List<String> output, StringBuilder str, int n, int open, int close) {

        if (open == n && close == n) {
            output.add(new String(str));
            return;
        }

        if (open < n) {
            str.append("(");
            backtrack(output, str, n, open + 1, close);
            str.deleteCharAt(str.length() - 1);
        }

           if (close < open) {
            str.append(")");
            backtrack(output, str, n, open, close + 1);
            str.deleteCharAt(str.length() - 1);
        }

    }
}
