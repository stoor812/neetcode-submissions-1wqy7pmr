# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        l1 = head
        l2 = None

        # FIND MIDDLE NODE
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        l2 = slow.next
        slow.next = None
        #REVERSE SECOND HALF
        prev = None
        curr = l2
        futr = None
        while curr:
            futr = curr.next
            curr.next = prev
            prev = curr
            curr = futr        
        l2 = prev

        #COMBINE LISTS
        while l2:
            t1 = l1.next
            t2 = l2.next

            l1.next = l2
            l2.next = t1

            l1 = t1
            l2 = t2


        



        

        