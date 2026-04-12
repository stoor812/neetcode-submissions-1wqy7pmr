# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        currHead = head
        count = 1

        # FIND LEN OF LIST
        while curr:
            length += 1
            curr = curr.next

        #EDGE CASE - RETURN EMPTY 
        if length == 1: return

        # REMOVE NTH NODE
        index = length - n
        curr = currHead

        #EDGE CASE - REMOVE FIRST NODE
        if index == 0:
            currHead = currHead.next
            return currHead


        while count < index:
            curr = curr.next
            count += 1
        
        temp1 = curr.next
        temp2 = temp1.next
        curr.next = temp2

        return currHead


        