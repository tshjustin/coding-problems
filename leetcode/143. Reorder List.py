# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        1. Split the list into 2 parts 

        2. reverse the second half 
            1l should have more elements 
            l2 should have the lesser number of elements 

        3. form the sol 
        """

        slow, fast = head, head 

        while fast.next and fast.next.next: 
            slow = slow.next # would point to the start of the second list
            fast = fast.next.next
        
        head2 = slow.next 
        slow.next = None 

        prev, cur = None, head2 
        while cur: 
            temp = cur.next 
            cur.next = prev 
            prev = cur 
            cur = temp 
        head2 = prev 
        

        cur1, cur2 = head, head2

        while cur2:
            temp1, temp2 = cur1.next, cur2.next
            
            cur1.next = cur2
            cur2.next = temp1
            
            cur1, cur2 = temp1, temp2

    