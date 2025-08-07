class MedianFinder:
    """
    Note that must be ordered ==> median (often ordered)

    brute force
    ----------
    maintain a sorted array ==> expensive 

    optimized 
    ----------
    when taking a median of a sorted array, we obtain 2 arrays: 

    1. smaller half of the array 

    2. larget half of the array


    [2, 3] => [2] [3] ==> median = largest element of the first array + smallest element of the second array

    [1, 2, 2 ,2, 4, 5 ,7] ==> [1, 2, 2, 2] [4, 5, 7] ==> take the top element 

    1. Since we need to maintain a sorted order --> cant use sorting of array (nlogn)

    2. hence use a heap (logn)

    3. maintain 2 heaps

    """
    # import heapq

    # def __init__(self):
    #     self.heap1 = [] # heap1 would store first half ==> [0, 1, 2...] ==> max heap ==> stores negative ==> python is min heap
    #     self.heap2 = [] # heap2 would store second half ==> [4, 5, 6...] ==> min heap

    # def addNum(self, num: int) -> None:
    #     """
    #     To decide which heap the current number goes in, must check the 

    #     1. min of the big heap 
    
    #     2. max of the small heap


    #     does not matter which heap we choose to add , just ensure that we maintain our heap choosing strategy


    #     Always note the size balancing, since we want each heap to be of roughly the same size ==> ensure that we perform rebalancing 
    #     """

    #     if not self.heap1 and not self.heap2:
    #         heapq.heappush(self.heap1, num)

    #     if not self.heap2:
    #         heapq.heappush(self.heap2, -num)

    #     elif num < self.heap1[0]: 
    #         heapq.heappush(self.heap1, num)

    #         if len(self.heap1) - len(self.heap2) > 1: # if the difference is greater than 1, then need to shift over the element 
    #             top_element = heapq.heappop(self.heap1)
    #             heapq.heappush(self.heap2, top_element)

    #     # else if the element is large, then we add to the larger heap 
    #     else:
    #         heapq.heappush(self.heap2, -num)

    #         if len(self.heap2) - len(self.heap1) > 1: # if the difference is greater than 1, then need to shift over the element 
    #             top_element = heapq.heappop(self.heap2)
    #             heapq.heappush(self.heap1, top_element)


    # def findMedian(self) -> float:

    #     # if we have an odd element, then we would look at the first array heap1 ==> since i designed it to store 1 more element in the case of odd
    #     if (len(self.heap1) + len(self.heap2)) % 2 == 1: 
    #         return float(self.heap1[0])

    #     return float((self.heap1[0] + self.heap2[0]) / 2)

    import heapq  

    def __init__(self):
        self.small = []  # max heap 
        self.large = []  # min heap
    
    def addNum(self, num: int) -> None:
        
        # alwasy add to small array 
        heapq.heappush(self.small, -num)
        
        # every num in small <= every num in large --> jsut check the last element -- perform this check all the time 
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        # balance the lengths 
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)
    
    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        return (-self.small[0] + self.large[0]) / 2.0

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()