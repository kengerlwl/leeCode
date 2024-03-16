import java.util.HashMap;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        if(s.length() <= 1){
            return s.length();
        }
        int left = 0;
        int right = 0;
        int ans = 1;
        HashMap<Character, Integer> map = new HashMap<>();
        map.put(s.charAt(left), 1);
        while (right < s.length()){
            if (left == right) {
                right++;
                if(right >= s.length()){
                    break;
                }
                map.put(s.charAt(left), 1);
            }

            // 放入map
            if (!map.containsKey(s.charAt(right))) {
                map.put(s.charAt(right), 1);
                ans = Math.max(ans, right - left + 1);
                right++;
            }else {// 如果已经存在，那么就要移动left
                // 越界判断
                if (right >= s.length() || left >= s.length()){
                    break;
                }

                while (s.charAt(left) != s.charAt(right) && left < right) {
                    map.remove(s.charAt(left));
                    left++;
                    
                }
                left++;
                right++;
            }
            // System.out.println("left: " + left + " right: " + right);
        }
        return ans;

    }
    // "dvdf"
    public static void main(String[] args) {
        Solution solution = new Solution();
        int ans = solution.lengthOfLongestSubstring("dvdf");
        System.out.println(ans);
    }


}