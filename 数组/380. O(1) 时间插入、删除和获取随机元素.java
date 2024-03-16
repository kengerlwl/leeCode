package 数组;

import java.util.HashSet;

import java.util.Iterator;
class RandomizedSet {
    HashSet<Integer> set;
    public RandomizedSet() {
         set = new HashSet<>();
    }
    
    public boolean insert(int val) {
        if(set.contains(val)) {
            return false;
        }
        set.add(val);
        return true;

    }
    
    public boolean remove(int val) {
        if(set.contains(val)) {
            set.remove(val);
            return true;
        }
        return false;
    }
    // 为了实现等概率的随机返回一个元素，我们可以使用一个哈希set和index来实现，随机游走
    public int getRandom() {
        int size = set.size();
        int index = (int)(Math.random() * size);
        Iterator<Integer> iterator = set.iterator();
        while(index-- > 0) {
            iterator.next();
        }
        return iterator.next();
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */