import java.util.Scanner;

// 注意类名必须为 Main, 不要有任何 package xxx 信息
public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        // 注意 hasNext 和 hasNextLine 的区别
        int n = in.nextInt();
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) {
            nums[i] = in.nextInt();
        }


        // 统计左右各自比该数更大的情况，最后只需要汇总，但是没时间了
        
        int[] leftLarger = new int[n];
        int[] leftSmaller = new int[n];
        int[] rightLarget = new int[n];
        int[] rightSmaller = new int[n];


        
    }
}