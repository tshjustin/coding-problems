# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        1. iterate until the kth element 

        2. reverse the nodes 

        3. Keep track of the pointer that points at the kth 
        """

        dummy = ListNode(0, head)
        prev_group = dummy # points to the node that is before 

        # traversing pointer 
        while True: 
            kth_node = self.get_k_node(prev_group, k) #  pointer to the kth node 

            # check if we have finished the list 
            if not kth_node:
                break

            next_group = kth_node.next 

        #     # now we need to reverse everything from the prev_group to the kth node 
        #     cur, prev = prev_group, None 

        #     while cur != next_group: 
        #         temp = cur.next 
        #         cur.next = prev
        #         prev = cur 
        #         cur = temp 

        #     # now link the initial head to the new_group 
        #     prev_group.next = next_group 
        #     prev_group = next_group 

        # return prev_group 

            prev, cur = kth_node.next, prev_group.next # prev defined as such so that it handles the first node (that is to be the last). to connect to the next group

            while cur != next_group: 
                temp = cur.next 
                cur.next = prev
                prev = cur 
                cur = temp 

            temp = prev_group.next  # note that this was pointed to the old head, which was [1], and not [3]
            prev_group.next = kth_node 
            prev_group = temp # prev_group would essentially just point to the node that is before next_group 
        
        return dummy.next 

    def get_k_node(self, cur, k): 
        while cur and k > 0: 
            cur = cur.next 
            k -=1 
        
        return cur

    

        