// public class ListNode {
//     int val;
//     ListNode next;
//     ListNode() {}
//     ListNode(int val) { this.val = val; }
//     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
// }



class Solution {
    public ListNode reverseBetween(ListNode head, int left, int right) {
        ListNode leftNode = head;
        ListNode leftPre = null;
        ListNode rightNode = head;
        for (int i = 0; i < left - 1; i++) {
            leftPre = leftNode;
            leftNode = leftNode.next;
        }
        for (int i = 0; i < right-1; i++) {
            rightNode = rightNode.next;
        }
        if(leftNode == rightNode){
            return head;
        }
        
        ListNode rightPost = rightNode.next;
        rightNode.next = null; // 先切断

        // 衔接左边的链表
        if (leftPre != null || leftNode == head) {
            
            if(leftPre != null){
                leftPre.next = null;
            }
            leftNode = reverse(leftNode);
            if(leftPre != null){
                leftPre.next = leftNode;
            }else{
                head = leftNode;
            }
        }

        ListNode cur = head;
        ListNode pre = null;
        while (cur != null) {
            pre = cur;
            cur = cur.next;
        }

        pre.next = rightPost;

        return head;





    }

    ListNode reverse(ListNode l){
        ListNode pre = null;
        ListNode cur = l;
        while (cur != null) {
            ListNode next = cur.next;
            cur.next = pre;
            pre = cur;
            cur = next;
        }
        return pre;

    }
}