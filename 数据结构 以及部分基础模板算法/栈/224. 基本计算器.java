import java.util.Stack;

class Solution {
    public int calculate(String s) {
        Stack<Integer> stackNum = new Stack<>();
        Stack<Character> stackOp = new Stack<>();
        s = s.replaceAll(" ", "");
        int len = s.length();
        // if (s.charAt(0) == '-') {
        //     stackNum.push(0);
        // }

        for (int i = 0; i < len; i++) {
            char tempC = s.charAt(i);
            if (tempC == ' ') {
                continue;
            }

            // System.out.println(stackNum);
            // System.out.println(stackOp);
            if (tempC =='(') {
                stackOp.push(tempC);
                continue;
            }

            if (tempC == '+' || tempC == '-') { //û�г˳����ÿ������ȼ�

                if (tempC == '-' && (i == 0 || s.charAt(i - 1) == '(' || s.charAt(i-1) == '+' || s.charAt(i-1) == '-')) { // ���������
                    stackNum.push(0);
                }
                
                while (!stackOp.isEmpty() && stackNum.size() >=2 && stackOp.peek() != '('){
                    int num2 = stackNum.pop();
                    int num1 = stackNum.pop();
                    char op = stackOp.pop();
                    if (op == '+') {
                        stackNum.push(num1 + num2);
                    } else {
                        stackNum.push(num1 - num2);
                    }
                }
                stackOp.push(tempC);
            } else if (tempC == ')') { // ���������žͽ��м���,Ҫ������������
                while (stackOp.peek() != '(') {
                    int num2 = stackNum.pop();
                    int num1 = stackNum.pop();
                    char op = stackOp.pop();
                    if (op == '+') {
                        stackNum.push(num1 + num2);
                    } else {
                        stackNum.push(num1 - num2);
                    }
                }
                stackOp.pop();
            } else { //����
                int num = 0;
                while (i < len && Character.isDigit(s.charAt(i))) {
                    num = num * 10 + s.charAt(i) - '0';
                    i++;
                }
                stackNum.push(num);
                i--;
            }
        }
        // ���ļ���
        while (!stackOp.isEmpty()) {
            int num2 = stackNum.pop();
            int num1 = stackNum.pop();
            char op = stackOp.pop();
            if (op == '+') {
                stackNum.push(num1 + num2);
            } else {
                stackNum.push(num1 - num2);
            }
        }
        return stackNum.pop();
    }

    /**
     * @param args
     */
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.calculate("- (3 + (4 + 5))"        ));
    }
}