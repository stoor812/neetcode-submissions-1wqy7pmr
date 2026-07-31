# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        while list1 and list2:
            #CHOOSE L1
            if list1.val <= list2.val:
                curr.next = list1
                curr = curr.next
                list1 = list1.next
            #CHOOSE L2
            else:
                curr.next = list2
                curr = curr.next
                list2 = list2.next
        
        # L1 APPEND REM
        if list1:
            curr.next = list1
        #L2 APPEND REM
        elif list2:
            curr.next = list2

        return dummy.next