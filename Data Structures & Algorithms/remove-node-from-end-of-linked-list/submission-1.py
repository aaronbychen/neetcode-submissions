# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        p = head
        while p:
            l += 1
            p = p.next
        p = head
        if l - n == 0:
            return head.next
        for i in range(0, l - n - 1):
            p = p.next
        p.next = p.next.next
        return head