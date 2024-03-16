public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int x = sc.nextInt();
    int y = sc.nextInt();
    int z = sc.nextInt();
    int yu = z%(3*x+y); //一个周期三天 成长值3*x+y ,
    int ans =0;
    if(yu==0) {
        ans = 3* (z/(3*x+y));
    }else {
        if(yu<x+y){
            ans = 3* (z/(3*x+y))+1;
        }
        else if(yu<2*x+y){
            ans = 3* (z/(3*x+y))+2;
        }else {
            ans = 3* (z/(3*x+y))+3;
        }
    }
    System.out.println(ans);
}
