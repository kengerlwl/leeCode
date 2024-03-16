package 数组;

class Solution {
    public String reverseWords(String s) {
        String[] words = s.split(" ");
        StringBuilder res = new StringBuilder(); // Java 中用于处理可变字符串的类，它提供了对字符串内容进行更改而不创建新的字符串对象的方法。这在需要频繁修改字符串时可以提高性能。
        for (int i = words.length - 1; i >= 0; i--) {
            if (words[i].equals("")) {
                continue;
            }
            res.append(words[i]).append(" ");
        }
        return res.toString().trim();
    }
}