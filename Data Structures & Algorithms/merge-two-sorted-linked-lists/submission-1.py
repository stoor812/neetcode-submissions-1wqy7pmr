# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        h_one = list1
        h_two = list2
        curr = None
        head = None

        if list1 is None: return list2
        if list2 is None: return list1

        if h_one.val <= h_two.val: #H1 less than or Equal
            curr = h_one
            h_one = h_one.next
        else:
            curr = h_two
            h_two = h_two.next

        head = curr #SET THE START OF THE LIST

        while True:
            if h_one is None and h_two: #END OF H1
                curr.next = h_two
                return head
            elif h_one and h_two is None: #End of H2
                curr.next = h_one
                curr = curr.next
                h_one = h_one.next
            elif h_one is None and h_two is None: #End of Both Lists
                return head
            elif h_one.val <= h_two.val:
                curr.next = h_one
                curr = curr.next
                h_one = h_one.next
            else:
                curr.next = h_two
                curr = curr.next
                h_two = h_two.next



        