// public class ListNode {
//     int val;
//     ListNode next;
//     ListNode() {}
//     ListNode(int val) { this.val = val; }
//     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
// }



class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int len1 = lenOfList(l1);
        int len2 = lenOfList(l2);

        // 保证l1是长的链表
        if (len1 < len2) {
            ListNode temp = l1;
            l1 = l2;
            l2 = temp;
        }

        // l1 = reverse(l1);
        // l2 = reverse(l2);
        ListNode start = l1;
        boolean addFlag = false;
        while (l1 != null) {
            int total = 0;
            if (l2!=null) {
                total = l1.val + l2.val;
                if (addFlag) {
                    total++;
                    addFlag = false;
                }

                l2 = l2.next;
            }else{
                total = l1.val;
                if (addFlag) {
                    total++;
                    addFlag = false;
                }
            }

            if (total >= 10) {
                addFlag = true;
                l1.val = total - 10;
            }else{
                l1.val = total;
            }

            // 如果已经是最后一个了，那么判断需不要加一个节点
            if (l1.next == null) {
                if (addFlag) {
                    ListNode temp = new ListNode(1);
                    l1.next = temp;
                    l1 = l1.next;
                }
                
            }
            l1 = l1.next;
        }

        return start;
        // return reverse(start);


        
    }

    int lenOfList(ListNode l) {
        int len = 0;
        while (l != null) {
            len++;
            l = l.next;
        }
        return len;
    }


    // 这个还是很有学习必要的。原地
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