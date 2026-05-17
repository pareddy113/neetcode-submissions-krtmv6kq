class Solution {
    public int evalRPN(String[] tokens) {
        
        ArrayDeque<Integer> stack = new ArrayDeque<>();

        int i = 0;
        while (i < tokens.length) {
            if ("+-*/".contains(tokens[i])) {
                Integer left = stack.pop();
                Integer right = stack.pop();
                Integer output = 0;
                switch(tokens[i]) {
                    case "+":
                        output = left + right;
                        break;
                    case "-":
                        output = right - left;
                        break;
                    case "*":
                        output = left * right;
                        break;
                    case "/":
                        output = right / left;
                        break;
                }
                System.out.println("left:" + left);
                System.out.println("right:" + right);
                System.out.println("output:" + output);
                stack.push(output);

            } else {
                System.out.println(Integer.valueOf(tokens[i]));
                stack.push(Integer.valueOf(tokens[i]));
            }
            i++;
        }
        return stack.pop();
    }
}
