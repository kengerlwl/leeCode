// package 双指针（移动窗口）;

class Solution {
    public int removeDuplicates(int[] nums) {
        int left = 0;
        int right = 0;
        int ans = 0;
        int writeIndex = 0;
        while (right < nums.length) {
            // 若相等，则右移
            if(nums[left] == nums[right]){
                right++;
            }
            else{
                // 计算区间长度
                if(right - left >= 3){ // 重复次数大于2,则需要删除,前进两个位置
                    ans += right - left - 2;
                    nums[writeIndex] = nums[left];
                    writeIndex++;
                    nums[writeIndex] = nums[left];
                    writeIndex++;

                }else{ // 重复次数小于等于2,则不需要删除,前进一个位置
                    for(int i = left; i < right; i++){
                        nums[writeIndex] = nums[i];
                        writeIndex++;
                    }
                }
                left = right;
            }
        }
        // 对于最后一个数字队列要也进行加上
        // 计算区间长度
        if(right - left >= 3){ // 重复次数大于2,则需要删除,前进两个位置
            ans += right - left - 2;
            nums[writeIndex] = nums[left];
            writeIndex++;
            nums[writeIndex] = nums[left];
            writeIndex++;

        }else{ // 重复次数小于等于2,则不需要删除,前进一个位置
            for(int i = left; i < right; i++){
                nums[writeIndex] = nums[i];
                writeIndex++;
            }
        }
        left = right;

        return nums.length - ans;
    }
}