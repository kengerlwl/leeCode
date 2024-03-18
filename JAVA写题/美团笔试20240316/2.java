import java.util.Scanner;

// 注意类名必须为 Main, 不要有任何 package xxx 信息
public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        // 注意 hasNext 和 hasNextLine 的区别
        String s = in.next();
        // lower 
        int ans1 = 0;
        for (int i = 0; i < s.length(); i++) {
            if(Character.isUpperCase(s.charAt(i))){
                ans1++;
            }
        }

        // all upper
        int ans2 = 0;
        for (int i = 0; i < s.length(); i++) {
            if(Character.isLowerCase(s.charAt(i))){
                ans2++;
            }
        }
        int ans3 = 0;
        if(Character.isLowerCase(s.charAt(0))){
            ans3++;
        }
        for (int i = 1; i < s.length(); i++) {
            if(Character.isUpperCase(s.charAt(i))){
                ans3++;
            }
        }

        System.out.println(Math.min(Math.min(ans1, ans2), ans3));
        


    }
}