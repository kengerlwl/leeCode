package 贪心;

// 在你的面前从左到右摆放着 nn 根长短不一的木棍，你每次可以折断一根木棍，并将折断后得到的两根木棍一左一右放在原来的位置（即若原木棍有左邻居，则两根新木棍必须放在左邻居的右边，若原木棍有右邻居，新木棍必须放在右邻居的左边，所有木棍保持左右排列）。折断后的两根木棍的长度必须为整数，且它们之和等于折断前的木棍长度。你希望最终从左到右的木棍长度单调不减，那么你需要折断多少次呢？

// 输入描述
// 第一行是一个数 nn，表示开始时有多少根木棍 (1<=n<=3000)(1<=n<=3000) 第二行有 nn 个数，从第 11 个到第 nn 个分别表示从左到右的木棍长度。对任意木棍的长度 ll，有 1<=l<=30001<=l<=3000。

// 输出描述
// 输出一行，一个数，你最少所需的折断木棍的次数 xx

// 示例

// 输入:
// 5
// 3 5 13 9 12

// 输出:
// 1
// 说明
// 你可以将长度为 1313 的木棍折成长度分别为 55 和 88 的两根木棍，最终得到的排列是 3 5 5 8 9 12


// 贪心就能解决啊
// 从后往前遍历，当当前位置木棍长度比后面的大时，就需要将其折成n份，策略是折成的n份中最小值尽量大，而最大值不超过后面的数。时间复杂度O(n) 空间复杂度O(1)


int fuc(vector<int>& heights){
    int n = heights.size();
    if(n == 0) return 0;
    int ans = 0, currHeight = heights[n-1];
    for(int i = n-2; i >= 0; --i){
        if(heights[i] <= currHeight){
            currHeight = heights[i];
        }else{
            if(heights[i] % currHeight == 0){
                int stick = heights[i] / currHeight;
                ans += stick - 1;
            }else{
                int stick = heights[i] / currHeight + 1;
                ans += stick - 1;
                currHeight = heights[i] / stick;
            }
        }
    }
    return ans;
}

