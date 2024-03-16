import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.Scanner;


// 注意类名必须为 Main, 不要有任何 package xxx 信息
public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int epoch = in.nextInt();
        // 注意 hasNext 和 hasNextLine 的区别
        for(int i =0; i < epoch; i++){
            int n = in.nextInt();
            int m = in.nextInt();
            Boolean flag = true;
            int[] nums = new int[n];
            for(int j = 0; j < n; j++){
                nums[j] = in.nextInt();
            }
            Integer[] nums2 = new Integer[n];
            for(int j = 0; j < n; j++){
                nums2[j] = in.nextInt();
            }
            Arrays.sort(nums);
            Arrays.sort(nums2, new Comparator<Integer>(){
                public int compare(Integer a, Integer b){
                        return b-a;
                }
        });

            for(int j = 0; j < n; j++){
                if (nums[j] + nums2[j] <= 0 || nums[j] + nums2[j] > m) {
                    System.out.println("No");
                    flag = false;
                    break;
                }
            }
            if (flag) {
                System.out.println("Yes");
            }
        }
   
    }
}