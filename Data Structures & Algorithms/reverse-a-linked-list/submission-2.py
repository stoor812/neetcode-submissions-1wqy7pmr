# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        futr = None

        while curr:
            futr = curr.next
            curr.next = prev
            prev = curr
            curr = futr

        return prev
        