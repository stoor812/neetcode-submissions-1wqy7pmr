# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        # SEPERATE SLOW / FAST BY N
        for i in range(n):
            fast = fast.next
        
        # ITERATE UNTIL FAST REACHES EOL
        while fast.next:
            slow = slow.next
            fast = fast.next

        # REMOVE N
        slow.next = slow.next.next
        

        return dummy.next