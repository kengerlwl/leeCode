package 数组;

class Solution {
    public String convert(String s, int numRows) {
        char[][] zTable = new char[numRows][s.length()];  // 其实没必要用二维数组，用numRows个StringBuilder就行了。我傻逼

        if(numRows == 1){
            return s;
        }

        int index = 0;
        for(int col =0; col < s.length(); col++){
            if(col % (numRows - 1) == 0){
                // 填充竖列
                for(int row = 0; row < numRows; row++){
                    zTable[row][col] = s.charAt(index);
                    index++;
                    if(index == s.length()){
                        break;
                    }
                }
                if(index == s.length()){
                    break;
                }
            }else{
                // 填充斜列
                zTable[numRows - 1 - col % (numRows - 1)][col] = s.charAt(index);
                index++;
                if (index == s.length()) {
                    break;
                    
                }
            }
            
        }

        StringBuilder res = new StringBuilder();
        for(int row = 0; row < numRows; row++){
            for(int col = 0; col < s.length(); col++){
                if(zTable[row][col] != 0){
                    res.append(zTable[row][col]);
                }
            }
        }

        return res.toString();
    }
}