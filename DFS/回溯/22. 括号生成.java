import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

class Solution {
    List<String> ans = new ArrayList<>();
    
    public List<String> generateParenthesis(int n) {
        Stack<Character> stack = new Stack<>();
        StringBuilder prefix = new StringBuilder();
        backTracking(stack, n, 0, 0, prefix);
        return ans;
    }

    // left: 用了几个左括号 right: 用了几个右括号
    public void backTracking(Stack<Character> stack, int n, int left, int right, StringBuilder prefix) {
        if (left == n && right == n) {
            ans.add(prefix.toString());
            return;
        }
        
        // 和之前的回溯不同，这边的分枝只有两种状态
        if (left < n) {
            stack.add('(');
            prefix.append('(');
            backTracking(stack, n, left + 1, right, prefix);
            stack.pop();
            prefix.deleteCharAt(prefix.length() - 1);
        }
        
        if (right < left) {
            stack.pop();
            prefix.append(')');
            backTracking(stack, n, left, right + 1, prefix);
            stack.push('(');
            prefix.deleteCharAt(prefix.length() - 1);
        }
    }

    // 输入：n = 3
    public static void main(String[] args) {
        Solution s = new Solution();
        s.generateParenthesis(3);
        System.out.println(s.ans);
    }
}
