class ListNode {
    int val;
    ListNode next;
    ListNode(int x) {
        val = x;
        next = null;
    }
}



public class Solution {
    public boolean hasCycle(ListNode head) {
        ListNode fast = head;
        ListNode slow = head;
        int count =0;
        if (fast == null) {
            return false;
        }
        fast = fast.next;

        
        if (fast == null) {
            return false;
        }
        while (fast != slow) {
            if (count > 30000) {
                break;

            }
            count++;
            fast = fast.next;
            if (fast == null) {
                return false;
            }
            fast = fast.next;
            if (fast == null) {
                return false;
            }
            slow = slow.next;
        }
        // System.out.println(fast.val)
        return fast == slow;
        
    }
}