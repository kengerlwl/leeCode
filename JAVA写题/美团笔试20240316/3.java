import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Scanner;

// 注意类名必须为 Main, 不要有任何 package xxx 信息
public class Main {

    
    public static HashMap<Integer, Long> map = new HashMap<>();

    public static long pow(int a, int y){
        if(map.containsKey(y)){
            return map.get(y);
        }

        if(y % 2 == 1){
            if(y == 1){
                map.put(y, (long)a);
                return (long)a;
            }
            map.put(y, ((long)a*pow(a, y-1)) % 1000000007);
            return ((long)a*pow(a, y-1)) % 1000000007;
        }else{ // 偶数
            if(y == 0){
                return 1;
            }else{
                map.put(y, ((long)pow(a, y/2) % 1000000007) * (pow(a, y/2) % 1000000007) % 1000000007);
                return ((long)pow(a, y/2) % 1000000007) * (pow(a, y/2) % 1000000007) % 1000000007;
            }
        }
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int q = in.nextInt();
        long mod = 1000000007;
        int[] nums = new int[n];
        int[] count = new int[n];

        for (int i = 0; i < n; i++) {
            nums[i] = in.nextInt();
        }

        for (int i = 0; i < n; i++) {
            count[i] = q;
        }
        for (int i = 0; i < q; i++) {
            int a = in.nextInt();
            count[a-1]-=1;
        }

        // count 得到了每个需要番的2的多少次
        long ans = 0;
        for (int i = 0; i < n; i++) {
            ans += ((long)nums[i] * (pow(2, count[i]) % mod))% mod;
            ans =  ans % mod;
        }
        System.out.println(ans);
        

    }
}


