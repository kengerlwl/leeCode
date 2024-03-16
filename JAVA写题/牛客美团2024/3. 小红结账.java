import java.util.Scanner;

// 注意类名必须为 Main, 不要有任何 package xxx 信息
public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        int n = in.nextInt();
        int m = in.nextInt();

        long[] peopelCost = new long[m+1];

        // 注意 hasNext 和 hasNextLine 的区别
        while (in.hasNextInt()) { // 注意 while 处理多个 case
            int peopleNum = in.nextInt();
            int totalCost = in.nextInt();
            double single = (double)totalCost / m;
            int singleCost = (totalCost-1)/peopleNum  +1;
            for(int i = 0; i< peopleNum-1; i++){
                int index = in.nextInt();
                peopelCost[index] += singleCost;
            }


            // System.out.println(a + b);
        }


        for(int i = 1; i <= m; i++){
            System.out.print(peopelCost[i]);
            if (i < m ) {
                System.out.print(" ");
            }
        }
        System.out.println();
    }
}