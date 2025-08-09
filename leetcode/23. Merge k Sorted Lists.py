# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        extract all the values into a heap 

        then form the final list 
        """ 

        import heapq 

        min_heap = []   

        for node in lists: 
            while node: 
                heapq.heappush(min_heap, node.val)
                node = node.next 


        dummy_head = ListNode(0) 
        cur = dummy_head 

        while min_heap: 
            current_val = heapq.heappop(min_heap)
            current_node = ListNode(current_val)
            
            cur.next = current_node 
            cur = cur.next 

        return dummy_head.next  

        