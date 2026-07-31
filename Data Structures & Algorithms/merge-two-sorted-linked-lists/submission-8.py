# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2
        dummy = ListNode()
        curr = dummy

        #BASE CASE:
        if list1 is None: return list2
        if list2 is None: return list1

        while head1 and head2:
            #CHOOSE L1
            if head1.val <= head2.val:
                curr.next = head1
                curr = curr.next
                head1 = head1.next
            #CHOOSE L2
            else:
                curr.next = head2
                curr = curr.next
                head2 = head2.next
        
        # L1 append
        if head1:
            curr.next = head1
        #L2 append
        elif head2:
            curr.next = head2

        return dummy.next

        
