import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;

class Solution {
    public HashSet<String> set = new HashSet<String>();

    // vis
    public HashSet<String> vis = new HashSet<String>();
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        for(String s: wordList){
            set.add(s);
        }
        if(!set.contains(endWord)){
            return 0;
        }
        int ans = 1;
        List<String> queue = new ArrayList<>();
        queue.add(beginWord);
        while (queue.size() != -1) {
            int size  = queue.size();
            for(int i = 0; i < size; i++){
                String cur = queue.remove(0); // 这里是remove(0)而不是remove(i)
                System.out.println("cur: " + cur);

                if(cur.equals(endWord)){
                    return ans;
                }
                for(int j = 0; j < cur.length(); j++){
                    // a-z
                    for(char c = 'a'; c <= 'z'; c++){
                        if(c == cur.charAt(j)){
                            continue;
                        }
                        String newString = cur.substring(0, j) + c + cur.substring(j + 1);
                        System.out.println("newString: " + newString);
                        if(set.contains(newString) && !vis.contains(newString)){
                            queue.add(newString);
                            vis.add(newString);
                        }
                    }
                }

                System.out.println("queue: " + queue);
            }
            ans++;
        }
        return 0;
    }

//     beginWord =
// beginWord =
// "hot"
// endWord =
// "dog"
// wordList =
// ["hot","dog"]

    public static void main(String[] args) {
        Solution s = new Solution();
        List<String> wordList = new ArrayList<>();
        wordList.add("hot");
        wordList.add("dog");
        System.out.println(s.ladderLength("hot", "dog", wordList));
    }
}