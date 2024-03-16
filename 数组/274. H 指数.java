package 数组;

import java.util.Arrays;

class Solution {
    public int hIndex(int[] citations) {
        // 先排序
        int n = citations.length;
        Arrays.sort(citations);

        for(int i = 0; i < n; i++){
            int h = n - i;
            if(citations[i] >= h){
                return h;
            }
        }
        return 0;

    }
}