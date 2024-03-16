class Solution {
    public ListNode sortList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        } else {
            ListNode slow = head;
            ListNode fast = head.next;
            while (fast != null && fast.next != null) { // 先分为两半
                slow = slow.next;
                fast = fast.next.next;
            }
            ListNode right = slow.next;
            slow.next = null;
            ListNode left = head;

            left = sortList(left);
            right = sortList(right);

            return merge(left, right);
        }
    }

    public ListNode merge(ListNode left, ListNode right) {
        ListNode dummy = new ListNode(0);
        ListNode cur = dummy;
        while (left != null && right != null) {
            if (left.val < right.val) {
                cur.next = left;
                left = left.next;
            } else {
                cur.next = right;
                right = right.next;
            }
            cur = cur.next;
        }
        if (left != null) {
            cur.next = left;
        }
        if (right != null) {
            cur.next = right;
        }
        return dummy.next;
    }
}
