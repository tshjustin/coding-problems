class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Brute force -> calculate for all possible points 


        Heap-methood: nlogn, but if we maintain only k elemnets in the heap, then we have nlogk


        max_heap = [] 

        for all elements inside the array: 
            calc distance

            if distance is smaller than the top element of the max heap: 
                heap pop 
                heap push 


        return heap 

        # store the data structure as (distance, [x, y])
        """

        import heapq 
        import math 

        heap = [] 

        for x, y in points: 

            distance = sqrt(x**2 + y**2)

            if len(heap) < k: 
                heapq.heappush(heap, (-distance, [x, y]))

            else: 

                # 
                if -distance > heap[0][0]: 
                    heapq.heappop(heap) 
                    heapq.heappush(heap, (-distance, [x ,y]))
        
        return [point for _, point in heap]


        