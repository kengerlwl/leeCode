import java.util.Arrays;
import java.util.Scanner;

// 注意类名必须为 Main, 不要有任何 package xxx 信息
class Main {

    public static int calPair(int[] nums, int k){
        // 暴力
        int[] nums2 = Arrays.copyOf(nums, nums.length);
        nums2[k] = -1 * nums[k];
        int n = nums.length;
        int ans =0;
        for (int i = 0; i < n; i++) {
            for (int j = i+1; j < n; j++) {
                // 逆序了
                if((nums[i] - nums[j]) * (nums2[i] - nums2[j]) < 0){
                    ans++;
                }
            }
            
        }
        return ans;

    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        // 注意 hasNext 和 hasNextLine 的区别
        int n = in.nextInt();
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) {
            nums[i] = in.nextInt();
        }


        for (int i = 0; i < n; i++) {
            System.out.print(calPair(nums, i));
            System.out.print(" ");
        }
        System.out.println();
    

        
    }
}