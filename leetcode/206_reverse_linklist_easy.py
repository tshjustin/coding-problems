# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # cur = head 
        # prev = None 

        # if not head:
        #     return None 

        """this code does not handle the last case - it disjoins then reconnects, but leaves an edge case for the last node """
        # while head: 
        #     head = head.next
        #     cur.next = prev 
        #     prev = cur 
        #     cur = head 

        # return head 

        if not head: 
            return None 

        """ dont use head as the traversal as it would be null at one point - leads to above case""" 

        cur, prev = head, None 

        while cur: 
            next_node = cur.next 
            cur.next = prev 
            prev = cur  
            cur = next_node 

        head = prev 

        return head 