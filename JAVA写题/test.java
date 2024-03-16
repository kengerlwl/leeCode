// 测试数据类型转换的demo， long和int

import java.util.ArrayList;
import java.util.List;

public class test {
    public static void main(String[] args) {
        List<Integer> list = new ArrayList<>();
        list.add(1);
        list.add(2);
        list.add(3);
        System.out.println(list);
        list.set(0, 349579345);
        System.out.println(list);
    }
}