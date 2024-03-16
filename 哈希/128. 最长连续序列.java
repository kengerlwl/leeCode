package 哈希;


// class Solution {
//     public int longestConsecutive(int[] nums) {
//         Set<Integer> num_set = new HashSet<Integer>();
//         for (int num : nums) {
//             num_set.add(num);
//         }

//         int longestStreak = 0;

//         for (int num : num_set) {
//             if (!num_set.contains(num - 1)) {
//                 int currentNum = num;
//                 int currentStreak = 1;

//                 while (num_set.contains(currentNum + 1)) {
//                     currentNum += 1;
//                     currentStreak += 1;
//                 }

//                 longestStreak = Math.max(longestStreak, currentStreak);
//             }
//         }

//         return longestStreak;
//     }
// }

// 作者：力扣官方题解
// 链接：https://leetcode.cn/problems/longest-consecutive-sequence/solutions/276931/zui-chang-lian-xu-xu-lie-by-leetcode-solution/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



// 这题对数据结构的的特性有一定考量，不能用红黑树的结构，得纯哈希，才能保证访问的效率是O(1)

import java.util.*;

class Solution {

    public int longestConsecutive(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();
        int ans = 0;
        for(int num : nums) {
            if (!map.containsKey(num)) {
                int left = map.getOrDefault(num - 1, num);
                int right = map.getOrDefault(num + 1, num);
                int len = right - left + 1;
                ans = Math.max(ans, len);
                map.put(num, num);
                map.put(left, right);
                map.put(right, left);
            }
        }
        return ans;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        int[] nums = {7,-9,3,-6,3,5,3,6,-2,-5,8,6,-4,-6,-4,-4,5,-9,2,7,0,0};
        System.out.println(s.longestConsecutive(nums));
    }
}
