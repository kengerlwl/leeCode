import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

class Solution {
    // 定义四个方向的偏移量，分别为上、下、左、右
    int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    // 在矩阵中查找单词
    public List<String> findWords(char[][] board, String[] words) {
        Trie trie = new Trie();
        // 将单词插入前缀树中
        for (String word : words) {
            trie.insert(word);
        }

        Set<String> ans = new HashSet<String>();
        // 遍历矩阵的每个位置
        for (int i = 0; i < board.length; ++i) {
            for (int j = 0; j < board[0].length; ++j) {
                // 深度优先搜索
                dfs(board, trie, i, j, ans);
            }
        }

        // 将结果转换为列表返回
        return new ArrayList<String>(ans);
    }

    // 深度优先搜索
    public void dfs(char[][] board, Trie now, int i1, int j1, Set<String> ans) {
        // 如果当前节点不在前缀树中，则返回
        if (!now.children.containsKey(board[i1][j1])) {
            return;
        }
        char ch = board[i1][j1];
        Trie nxt = now.children.get(ch);
        // 如果当前节点是单词的结尾，则将单词加入结果集
        if (!"".equals(nxt.word)) {
            ans.add(nxt.word);
            nxt.word = "";
        }

        // 如果当前节点还有子节点，继续深度优先搜索
        if (!nxt.children.isEmpty()) {
            board[i1][j1] = '#';
            for (int[] dir : dirs) {
                int i2 = i1 + dir[0], j2 = j1 + dir[1];
                if (i2 >= 0 && i2 < board.length && j2 >= 0 && j2 < board[0].length) {
                    dfs(board, nxt, i2, j2, ans);
                }
            }
            board[i1][j1] = ch;
        }

        // 如果当前节点没有子节点，移除当前节点
        if (nxt.children.isEmpty()) {
            now.children.remove(ch);
        }
    }
}

// 前缀树节点
class Trie {
    String word;
    Map<Character, Trie> children;

    // 初始化前缀树节点
    public Trie() {
        this.word = "";
        this.children = new HashMap<Character, Trie>();
    }

    // 插入单词到前缀树中
    public void insert(String word) {
        Trie cur = this;
        for (int i = 0; i < word.length(); ++i) {
            char c = word.charAt(i);
            if (!cur.children.containsKey(c)) {
                cur.children.put(c, new Trie());
            }
            cur = cur.children.get(c);
        }
        cur.word = word;
    }
}
