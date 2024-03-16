import java.util.HashMap;

class Solution {
    public String minWindow(String s, String t) {
        HashMap<Character, Integer> map = new HashMap<>();
        for(int i =0; i < t.length(); i++){
            Character c = t.charAt(i);
            if(map.containsKey(c)){
                map.put(c, map.get(c)+1);
            }else{
                map.put(c, 1);
            }
        }

        HashMap<Character, Integer> cur = new HashMap<>();
        // 初始化为0
        for(Character c: map.keySet()){
            cur.put(c, 0);
        }
        int left = 0;
        int right = 0;
        int n = s.length();
        int minLen = Integer.MAX_VALUE;
        String ans = "";
        while (right < n) {
            // if ok
            if(judgeOK(map, cur)){
                int nowLen = right - left +1;
                if (nowLen < minLen){
                    minLen = nowLen;
                    ans = s.substring(left, right+1);

                }

                Character c = s.charAt(left);
                if (map.containsKey(c)) {
                    map.put(c, map.get(c)-1);
                }
                left++;

            }else{
                Character c = s.charAt(right);
                if (map.containsKey(c)) {
                    map.put(c, map.get(c)+1);
                }
                right++;
            }
            System.out.println("left: " + left + " right: " + right);
        }
        return ans;



    }


    public static boolean judgeOK(HashMap<Character, Integer> map, HashMap<Character, Integer> cur){
        boolean ans = true;
        for(Character c: map.keySet()){
            if(cur.get(c) < map.get(c)){
                ans = false;
                break;
            }
        }
        return ans;
    }

    // s = "ADOBECODEBANC", t = "ABC"
    public static void main(String[] args) {
        Solution solution = new Solution();
        String ans = solution.minWindow("ADOBECODEBANC",  "ABC");
        System.out.println(ans);
    }
}