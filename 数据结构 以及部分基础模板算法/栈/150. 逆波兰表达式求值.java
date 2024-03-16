import java.util.Stack;

class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stackNum = new Stack<>();
        // Stack<String> stackOp = new Stack<>();
        for (int i = 0; i < tokens.length; i++) {
            String tempS = tokens[i];
            if (tempS.equals("+") || tempS.equals("-") || tempS.equals("*") || tempS.equals("/")) { // 逆波兰遵循的是后缀表达式，所以遇到操作符就进行计算
                int num2 = stackNum.pop();
                int num1 = stackNum.pop();
                if (tempS.equals("+")) {
                    stackNum.push(num1 + num2);
                } else if (tempS.equals("-")) {
                    stackNum.push(num1 - num2);
                } else if (tempS.equals("*")) {
                    stackNum.push(num1 * num2);
                } else if (tempS.equals("/")) {
                    stackNum.push(num1 / num2);
                }
            } else {
                stackNum.push(Integer.parseInt(tempS));
            }
        }

       
        return stackNum.pop();
    }

    // ["2","1","+","3","*"]
    public static void main(String[] args) {
        Solution s = new Solution();
        String[] tokens = new String[]{"2","1","+","3","*"};
        System.out.println(s.evalRPN(tokens));
    }


}