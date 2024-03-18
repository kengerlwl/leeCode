import java.util.HashMap;
import java.util.Scanner;

// 注意类名必须为 Main, 不要有任何 package xxx 信息
public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        // 注意 hasNext 和 hasNextLine 的区别
        int n = in.nextInt();
        int[] nums = new int[n];
        int[] preSum = new int[n];

        // 计算所有子区间的和的数量
        HashMap<Integer, Integer> count = new HashMap<>();
        HashMap<Integer, Integer> newcount = new HashMap<>();

        for (int i = 0; i < n; i++) {
            nums[i] = in.nextInt();
            if(nums[i] == 2){
                nums[i] = 1;
            }else{
                nums[i] = -1;
            }
            
        }
        preSum[0] = nums[0];
        for (int i = 1; i < n; i++) {
            preSum[i] = preSum[i-1] + nums[i];
        }

        // init side
        count.put(preSum[0], 1);
        

        int num2 = 0;
        int num1 = 0;

        if(preSum[0] == 1){
            num2 =1;
        }else{
            num1 =1;
        }

        // start search
        for (int i = 1; i < n; i++) {
            newcount = new HashMap<>();
            for(int j : count.keySet()){
                int next = j+1;
                newcount.put(next, count.get(j));
            }
            if(newcount.containsKey(nums[i])){
                newcount.put(nums[i], newcount.get(nums[i])+1);
            }
            else{
                newcount.put(nums[i], 1);
            }

            for(int j : newcount.keySet()){
                if(j>0){
                    num2 += newcount.get(j);
                }else{
                    num1 += newcount.get(j);
                }
            }
            count = newcount;
            
        }

        System.out.println(num1 + num2 * 2);
        
        
    }
}