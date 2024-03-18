import java.util.Scanner;

// 注意类名必须为 Main, 不要有任何 package xxx 信息
public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] nums = new int[n];
        long sum = 0;
        for (int i = 0; i < n; i++) {
            nums[i] = in.nextInt();
            sum+= nums[i];
        }
        int x = in.nextInt();
        int y = in.nextInt();

        System.out.println(sum - x -y);
        


    }
}