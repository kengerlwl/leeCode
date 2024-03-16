import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;


// 那么一个直观的思路是：

// 使用哈希表 map 记录 words 中每个单词的出现次数
// 枚举 s 中的每个字符作为起点，往后取得长度为 m×wm \times wm×w 的子串 sub
// 使用哈希表 cur 统计 sub 每个单词的出现次数（每隔 w 长度作为一个单词）
// 比较 cur 和 map 是否相同
// 注意：在步骤 333 中，如果发现 sub 中包含了 words 没有出现的单词，可以直接剪枝。


class Solution {
    public List<Integer> findSubstring(String s, String[] words) {
        int n = s.length(), m = words.length, w = words[0].length();
        Map<String, Integer> map = new HashMap<>();
        for (String word : words) map.put(word, map.getOrDefault(word, 0) + 1);
        List<Integer> ans = new ArrayList<>();
        out:for (int i = 0; i + m * w <= n; i++) {
            Map<String, Integer> cur = new HashMap<>();
            String sub = s.substring(i, i + m * w);
            for (int j = 0; j < sub.length(); j += w) {
                String item = sub.substring(j, j + w);
                if (!map.containsKey(item)) continue out;
                cur.put(item, cur.getOrDefault(item, 0) + 1);
            }
            if (cur.equals(map)) ans.add(i);
        }
        return ans;
    }
}

