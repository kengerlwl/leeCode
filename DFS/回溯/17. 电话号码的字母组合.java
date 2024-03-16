package DFS.回溯;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Set;


// 回溯
class Solution {
    public HashMap<Integer, List<Character>> num2char =  new HashMap<>();
    public Set<String> ans = new HashSet<>();
    public List<String> letterCombinations(String digits) {
        if (digits.length() == 0) {
            return new ArrayList<String>();
            
        }

        // init the map
        for(int i = 2; i <= 9; i++){
            num2char.put(i, new ArrayList<Character>());
        }
        num2char.get(2).add('a');
        num2char.get(2).add('b');
        num2char.get(2).add('c');
        num2char.get(3).add('d');
        num2char.get(3).add('e');
        num2char.get(3).add('f');
        num2char.get(4).add('g');
        num2char.get(4).add('h');
        num2char.get(4).add('i');
        num2char.get(5).add('j');
        num2char.get(5).add('k');
        num2char.get(5).add('l');
        num2char.get(6).add('m');
        num2char.get(6).add('n');
        num2char.get(6).add('o');
        num2char.get(7).add('p');
        num2char.get(7).add('q');
        num2char.get(7).add('r');
        num2char.get(7).add('s');
        num2char.get(8).add('t');
        num2char.get(8).add('u');
        num2char.get(8).add('v');
        num2char.get(9).add('w');
        num2char.get(9).add('x');
        num2char.get(9).add('y');
        num2char.get(9).add('z');

        back_tracking(digits, "");

        List<String> ret = new ArrayList<>();
        for(String s: ans){
            ret.add(s);
        }
        return ret;


    }


    public void back_tracking(String s, String prefix){
        // System.out.println("s: " + s + " prefix: " + prefix);
        if (s.length() == 0) {
            ans.add(prefix);
            return;
        }
        for(Character c: num2char.get(s.charAt(0)-'0')){
            back_tracking(s.substring(1), prefix.concat(c.toString()));
        }
    }
    // "23"
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.letterCombinations("23"));
    }
}