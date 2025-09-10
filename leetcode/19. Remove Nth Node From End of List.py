# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Create a gap of n between left and right 

        When right is exhausted (at the end of the LL), then left would be n from behind the LL

        """
        dummy = ListNode(0, head)
        left = dummy 
        right = head 

        while n > 0: 
            right = right.next
            n -= 1

        while right: 
            left = left.next
            right = right.next 

        left.next = left.next.next

        return dummy.next
        