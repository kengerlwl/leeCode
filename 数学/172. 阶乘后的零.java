package 数学;

import java.util.HashMap;

class Solution {
    public int trailingZeroes(int n) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int i = 1; i <= n; i++){
            int temp = i;
            // 判断temp是不是10的倍数
            while(temp % 10 == 0){
                temp = temp / 10;
                if(map.containsKey(10)){
                    map.put(10, map.get(10) + 1);
                }else{
                    map.put(10, 1);
                }
            }
            // 判断temp是不是2的倍数
            while(temp % 2 == 0){
                temp = temp / 2;
                if(map.containsKey(2)){
                    map.put(2, map.get(2) + 1);
                }else{
                    map.put(2, 1);
                }
            }
            // 判断temp是不是5的倍数
            while(temp % 5 == 0){
                temp = temp / 5;
                if(map.containsKey(5)){
                    map.put(5, map.get(5) + 1);
                }else{
                    map.put(5, 1);
                }
            }


        }
        if(map.containsKey(2) && map.containsKey(5)){
            return Math.min(map.getOrDefault(2, 0), map.getOrDefault(5, 0)) + map.getOrDefault(10, 0);
        }else{
            return map.getOrDefault(10, 0);
        }
    }
}