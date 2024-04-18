class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param head ListNode类 
# @return ListNode类
#
class Solution:
    def ReverseList(self , head: ListNode) -> ListNode:
        # write code here
        dummpy = ListNode(-1)
        # 基于递归实现不占用一个新数组，但是好像递归沾也占用了大量的存储。
        cur = head
        next = cur.next

        cur.next = None
        while next:
            tmpNext = next.next
            next.next = cur

            cur = next
            next = tmpNext
        
        return cur