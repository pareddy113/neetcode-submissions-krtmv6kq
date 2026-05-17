class Solution {
    public int evalRPN(String[] tokens) {
        
        ArrayDeque<Integer> stack = new ArrayDeque<>();

        int i = 0;
        while (i < tokens.length) {
            if ("+-*/".contains(tokens[i])) {
                Integer left = stack.pop();
                Integer right = stack.pop();
                switch(tokens[i]) {
                    case "+":
                        stack.push(right + left);
                        break;
                    case "-":
                        stack.push(right - left);
                        break;
                    case "*":
                        stack.push(right * left);
                        break;
                    case "/":
                        stack.push(right / left);
                        break;
                }
                

            } else {
                stack.push(Integer.valueOf(tokens[i]));
            }
            i++;
        }
        return stack.pop();
    }
}
