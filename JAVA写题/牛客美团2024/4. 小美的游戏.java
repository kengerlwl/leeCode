import java.util.PriorityQueue;
import java.util.Scanner;
import java.util.Comparator;

// 注意类名必须为 Main, 不要有任何 package xxx 信息
public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int k = in.nextInt();
        PriorityQueue<Integer> pq = new PriorityQueue<>(Comparator.reverseOrder());
        int[] nums = new int[n=1];
        int index = 1;
        // 注意 hasNext 和 hasNextLine 的区别
        while (in.hasNextInt()) { // 注意 while 处理多个 case
            int a = in.nextInt();
            nums[index] = a;
            index++;
            pq.add(a);
        }

        int now = pq.poll();
        pq.add(1);
        for(int i = 0; i < k && pq.size()>0; i++){
            int a = pq.poll();
            now *= a;
        }

        while (pq.size() > 0) {
            now*=pq.poll();
        }

        System.out.println(now);
        
    }
}