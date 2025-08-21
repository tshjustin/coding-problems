class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Trivial to traverse the array 

        But checking the maximum number is the problematic bit 

        Brute force --> O(k) for each window , for x windows --> O(KX)

        --------
        Since we need to keep tracking the maximum elements, what we can do is 
        to keep tracking the elements inside a heap 

        ==> O(1) peek 
        ==> log(n) insertion 

        But the tricky part is knowing if we are still inside the window or not 

        ----------
        1. Maintain a heap with all the elements and their index 

        2. For each window --> we would have a range of elements 

        3. Items that bubble up to the top 
            a. if they are greater than the current window index, recyle them 
            b. else throw them away 


        ---------------------
        1. As we proceed, build the heap 

        2. If we have a valid window --> meaning that we added enough elements

        3. then we remove the top element ==> add to soltuion 

        4. For the next element, once we get the heap again, we need to clean the old elements out 
            --> which we can do by just adding a while loop on the idx check 
        """

        import heapq 

        heap = []
        sol = []

        for i in range(len(nums)): 

            heapq.heappush(heap, (-nums[i], i))

            # for the first window 
            if i >= k-1: 

                # clean the expired elements --> just check that the elements are within window 
                while heap[0][1] < i - k + 1:
                    heapq.heappop(heap)     

                sol.append(-heap[0][0])

        return sol 

        



        