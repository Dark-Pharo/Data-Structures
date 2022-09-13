class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution():
    def reversll(self, head: ListNode) -> ListNode:

        pre = None
        cur = head
        suc = None

        while cur:
            suc = cur.next
            cur.next = pre
            pre = cur
            cur = suc
            
        return pre