class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        h = ListNode(0)
        e = ListNode(None)
        while head.next:
            tmp = ListNode(None)
            print(head.val)
            h.val = head.val
            h.next = tmp

