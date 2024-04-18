class MyItem():
    def __init__(self, node=None):
        self.node = node
    def __lt__(self, other):
        return self.node.val < other.node.val


import collections
import queue
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        pq = queue.PriorityQueue()
        for node in lists:
            pq.put(MyItem(node))
        dummpy = ListNode(-1, None)
        cur = dummpy
        while not pq.empty():
            item = pq.get()
            node = item.node
            cur.next = node
            cur = cur.next
            if node.next:
                pq.put(MyItem(node.next))

        return dummpy.next