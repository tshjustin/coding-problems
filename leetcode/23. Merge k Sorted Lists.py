# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    #     """
    #     extract all the values into a heap 

    #     then form the final list 
    #     """ 

    #     import heapq 

    #     min_heap = []   

    #     for node in lists: 
    #         while node: 
    #             heapq.heappush(min_heap, node.val)
    #             node = node.next 


    #     dummy_head = ListNode(0) 
    #     cur = dummy_head 

    #     while min_heap: 
    #         current_val = heapq.heappop(min_heap)
    #         current_node = ListNode(current_val)
            
    #         cur.next = current_node 
    #         cur = cur.next 

    #     return dummy_head.next  

     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Extract all the values into a heap 

        Then start popping 

        O(nlogn)


        optimized 
        ---------
        Another optimzied version is that we maintain just k values in the heap, where each element 
        is contributed by each of the k list 
        """

        # import heapq

        # heap = []  # min heap

        # # Push the head of each list into the heap
        # for l in lists:
        #     if l:
        #         heapq.heappush(heap, (l.val, id(l), l))

        # dummy_head = ListNode(0)
        # cur = dummy_head

        # while heap:
        #     val, _, node = heapq.heappop(heap)
        #     cur.next = node
        #     cur = cur.next

        #     # If the node has a next, push it into the heap
        #     if node.next:
        #         heapq.heappush(heap, (node.next.val, id(node.next), node.next))

        # return dummy_head.next

        """
        Think of merge sort,

        1. combine singular elements 
        2. merge them, then sort --> [1 5] [6 2] --> 1 2 5 6
        3. repeat until we finish


        """

        if not lists or len(lists) == 0:
            return None 

        while len(lists) > 1: 
            # keep reducing the list, half at a time 

            mergedLists = []

            # take pairs of linkedlist 
            for i in range(0, len(lists), 2): 
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None # could be OOB since odd number of lists 

                # merge the 2 lists together
                mergedLists.append(self.mergeList(l1, l2))

            lists = mergedLists 

        # would have one list left, that is the solution 
        return lists[0]

    def mergeList(self, l1, l2):
        """
        Now we just perform a merge of the 2 link list  --> trivial 
        """

        dummy = ListNode()
        tail = dummy 

        while l1 and l2: 
            if l1.val < l2.val: 
                tail.next = l1 
                l1 = l1.next 

            else: 
                tail.next = l2 
                l2 = l2.next 

            tail = tail.next 

        tail.next = l1 or l2 

        return dummy.next
    # N log k 