// 关键是节点的分叉数量，以及游走，其中节点的分叉建议用HashMap。更加好用

import java.util.HashMap;


class TrieNode {
    HashMap<Character, TrieNode> children;
    boolean isEndOfWord;

    public TrieNode() {
        children = new HashMap<>();
        isEndOfWord = false;
    }
}

class WordDictionary {
    private TrieNode root;

    public WordDictionary() {
        root = new TrieNode();
    }
    
    public void addWord(String word) {
        TrieNode current = root;
        for (int i = 0; i < word.length(); i++) {
            char ch = word.charAt(i);

            // 获取子节点，如果没有则创建
            TrieNode node = current.children.get(ch);
            if (node == null) {
                node = new TrieNode();
                current.children.put(ch, node);
            }
            current = node;
        }
        current.isEndOfWord = true;

    }
    
    public boolean search(String word) {
        return startsWith(word, root);
    }

    // 递归的方式实现
    public boolean startsWith(String prefix, TrieNode root) {
        TrieNode current = root;
        for (int i = 0; i < prefix.length(); i++) {
            char ch = prefix.charAt(i);
            if (ch == '.') {
                for (TrieNode node : current.children.values()) {
                    if (startsWith(prefix.substring(i + 1), node)) {
                        return true;
                    }
                }
                return false;
            }
            else {
                TrieNode node = current.children.get(ch);
                if (node == null) {
                    return false;
                }
                current = node;
            }
        }
        return current.isEndOfWord;
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * boolean param_2 = obj.search(word);
 */