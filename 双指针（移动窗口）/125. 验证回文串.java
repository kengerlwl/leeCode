class Solution {
    public boolean isPalindrome(String s) {
        int  left = 0;
        int right = s.length() - 1;
        boolean ans = true;
        while (left < right) {
            char leftChar = s.charAt(left);
            char rightChar = s.charAt(right);
            leftChar = Character.toLowerCase(leftChar);
            rightChar = Character.toLowerCase(rightChar);
            if (leftChar < '0' || leftChar > '9' && leftChar < 'a' || leftChar > 'z') {
                left++;
                continue;
                
            }
            if (rightChar < '0' || rightChar > '9' && rightChar < 'a' || rightChar > 'z') {
                right--;
                continue;
                
            }
            // 两个字符都是数字或者字母
            if(leftChar != rightChar){
                ans = false;
                break;
            }
            left++;
            right--;
            
        }

        return ans;

    }
}