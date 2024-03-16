import java.util.HashMap;
import java.util.HashSet;
import java.util.Scanner;

// 注意类名必须为 Main, 不要有任何 package xxx 信息
public class Main {
    public static HashMap<Integer, Boolean> countMap = new HashMap<>();
    public static HashSet<Integer> leftNum = new HashSet<>();
    public static Boolean flag = true;
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int m = in.nextInt();

        int count = 0;
        int step = 0;
        for(int i =1; i <= n; i++){
            countMap.put(i, false);
            leftNum.add(i);
        }



        // 注意 hasNext 和 hasNextLine 的区别
        while (in.hasNextInt()) { // 注意 while 处理多个 case
            int a = in.nextInt();
            int b = in.nextInt();
            // System.out.println(a + b);
            step++;
            if (count >= n) {
                continue;
            }
            if (a == 1) {
                // b false
                if (leftNum.contains(b)) {
                    count++;
                    // countMap.put(b, true);
                    leftNum.remove(b);
                }
            }else{

                // 还剩下b没有
                if (leftNum.contains(b)) {
                    HashSet<Integer> temp = new HashSet<>();
                    temp.add(b);
                    leftNum = temp;
                    count = n-1;

                }else{
                    count = n;
                    leftNum = new HashSet<>();
                    count = n;
                }

                // for(int i = 1; i <= n; i++){
                //     if (!countMap.get(i) && i != b) {
                //         count++;
                //         countMap.put(i, true);
                        
                //     }
                // }
            }
            


            if (count == n && flag) {
                flag = false;
                System.out.println(step);
            }
        }


        if (count < n && flag){
            flag = false;
            System.out.println(-1);
        }


    }



}