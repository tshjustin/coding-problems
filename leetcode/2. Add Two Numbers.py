# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        123 --> 3 -> 2 -> 1


        try 
        -----
        1. reverse the each list --> redundant 
        2. traverse and sum using the *10 rule 
        3. find the sum of both 
        4. create the actual linked list 


        1 2 3 ==> 123 

        Note that if we have 1 2 3 ==>

        3 * 10^0 = 3 
        2 * 10^1 = 20 
        1 * 10^2 = 100 

        100 + 20 + 3 = 123 ==> No need to reverse in the first place 

        """

        # def reverse(head): 
        #     prev, cur = None, head 

        #     while cur: 
        #         temp = cur.next 
        #         cur.next = prev 
        #         prev = cur 
        #         cur = temp 
        #     return prev 

        def summation(head): 
            prefix = 0 
            total = 0 

            while head: 
                value = head.val 
                total += value * 10**(prefix)
                prefix +=1 
                head = head.next 

            return total 
                
        sum_1 = summation(l1)
        sum_2 = summation(l2)

        result = str(sum_1 + sum_2)
        
        dummy = ListNode(0)
        cur = dummy 

        for digit in result[::-1]: 
            new_node = ListNode(digit)

            cur.next = new_node 
            cur = cur.next 

        return dummy.next 














