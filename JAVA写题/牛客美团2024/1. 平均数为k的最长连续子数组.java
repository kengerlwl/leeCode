package 牛客美团2024;
import java.util.*;

// 注意类名必须为 Main, 不要有任何 package xxx 信息
public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt(), k = in.nextInt();
        long[] nums = new long[n + 1];
        int i = 0, ans = -1;
        Map<Long, Integer> map = new HashMap<>();
        map.put(0L, 0);
        // 注意 hasNext 和 hasNextLine 的区别
        while (in.hasNextInt()) { // 注意 while 处理多个 case
            nums[++i] += in.nextInt() - k + nums[i - 1]; // 减去k变成不需要平均值
            if(!map.containsKey(nums[i])) map.put(nums[i], i);
            else ans = Math.max(ans, i - map.get(nums[i]));
        }
        System.out.println(ans);
    }
}
