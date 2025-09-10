# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        1. instantiate a dummy head node 

        2. This head node would point to the first node of the LL 

        init dummy node 

        while p1 and p2: 
            if p1.val >= p2.val: 
                append p2.val 
                increment p2 

            else: 
                append p1.val
                incremenet p1

        if p1:
            append the rest 

        if p2: 
            append the rest 
        """
        
        # dummy head 
        dummy_head = ListNode()
        cur = dummy_head 

        # these are pointers to the head node already
        while list1 and list2: 

            if list1.val >= list2.val: 
                cur.next = list2 # this means that cur.next would point to the NODE that is pointed by list2
                list2 = list2.next # increment list2 

            else: 
                cur.next = list1
                list1 = list1.next 

            cur = cur.next 
            
        if list1: 
            cur.next = list1 

        if list2:
            cur.next = list2

        return dummy_head.next 