# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        prev = None
        curr = head
        futr = None

        while curr:
            if curr.next == None: # End of List
                curr.next = prev
                return curr
            else:
                futr = curr.next

                curr.next = prev
                prev = curr
                curr = futr
                futr = futr.next

        return curr
        