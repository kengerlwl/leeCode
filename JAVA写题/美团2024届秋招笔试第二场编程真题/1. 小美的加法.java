import java.util.Scanner;

// 注意类名必须为 Main, 不要有任何 package xxx 信息
public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        long[] nums = new long[n];
        long[] preSum = new long[n];
        long[] postSum = new long[n];
        for (int i = 0; i < n; i++) {
            long a = in.nextLong();
            nums[i] = a;
        }
        preSum[0] = nums[0];
        for (int i = 1; i < n; i++) {
            preSum[i] = preSum[i - 1] + nums[i];
        }
        postSum[n - 1] = nums[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            postSum[i] = postSum[i + 1] + nums[i];
        }

        long ans = 0;
        if (n == 2) {
            System.out.println(nums[0] * nums[1]);
        } else {
            ans = nums[0] * nums[1] + postSum[2];
            ans = Math.max(ans, nums[n - 1] * nums[n - 2] + preSum[n - 3]);

            for (int i = 1; i <= n - 3; i++) {
                ans = Math.max(ans, nums[i] * nums[i + 1] + preSum[i - 1] + postSum[i + 2]);

            }
            System.out.println(ans);
        }

    }
}