# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head


        index = 1
        dummy = head

        list1 = head
        list2 = None

        # SPLIT LIST
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        list2 = slow.next
        slow.next = None

        #REVERSE L2
        prev = None
        curr = list2
        nxt = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        list2 = prev

        while list1 and list2:
            if index == 1:
                tmp1 = list1.next
                list1.next = list2
                list1 = tmp1
                index = 2
            else:
                tmp2 = list2.next
                list2.next = list1
                list2 = tmp2
                index = 1


            

            