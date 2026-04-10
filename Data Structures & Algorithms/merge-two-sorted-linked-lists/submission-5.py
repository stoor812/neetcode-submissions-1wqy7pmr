# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        curr = head

        if list1 is None: return list2
        if list2 is None: return list1

      #  if list1.val <= list2.val: #H1 less than or Equal
     #       curr = list1
     #       list1 = list1.next
      #  else:
     #       curr = list2
     #       list2 = list2.next

     #   head = curr #SET THE START OF THE LIST

        while True:
            if list1 is None and list2: #END OF H1
                curr.next = list2
                return head.next
            elif list1 and list2 is None: #End of H2
                curr.next = list1
                return head.next
            elif list1 is None and list2 is None: #End of Both Lists
                return head.next
            elif list1.val <= list2.val:
                curr.next = list1
                curr = curr.next
                list1 = list1.next
            else:
                curr.next = list2
                curr = curr.next
                list2 = list2.next



        