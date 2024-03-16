package top100;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

class Solution {

    // 将字符串排序后作为key
    public String calKey(String s){
        char[] c = s.toCharArray();
        Arrays.sort(c);
        return new String(c);
    }

    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> map = new HashMap<>();
        for(String s : strs){
            String key = calKey(s);
            if(map.containsKey(key)){
                map.get(key).add(s);
            }else{
                List<String> list = new ArrayList<>();
                list.add(s);
                map.put(key, list);
            }
        }

        // 将map中的值转化为list
        List<List<String>> ans = new ArrayList<>();
        for(List<String> list : map.values()){
            ans.add(list);
        }
        return ans;


    }
}