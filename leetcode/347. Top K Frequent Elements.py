class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """  
        just use a hash map to count 

        then iterate with a heap 

        space = O(n+k)
        time = O(n + nlogk)



        Another solution 
        ----------------
        bucket sort ==> 

        1. form buckets, where each unique element is a bucket 
        2. iterate array, increment the counter of that element in that bucket 
        3. return the topk --> but this is the tricky part 

        a. instead of each element = 1 bucket 
        b. use an array where i = count of the elemnent, arr[i] = elements themselves (arr) 
        c. hence the most frquency element would be the largest i 
        """
        # from collections import defaultdict 

        # hash_map = defaultdict(int)

        # for num in nums: 
        #     hash_map[num] += 1

        # import heapq # use min heap to take the top k elements counts 
        # heap = []

        # for key, value in hash_map.items(): 

        #     if len(heap) < k: 
        #         heapq.heappush(heap, (value, key))

        #     else: 
        #         if heap[0][0] < value:  # the top of the heap is the smallest of the k 
        #             heapq.heappop(heap)
        #             heapq.heappush(heap, (value, key))

        # sol = []
        # for val, key in heap: 
        #     sol.append(key)

        # return sol 

        from collections import defaultdict 

        count = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)] # Note that frequency of element <= total number of eleemnts ==> [7,7,7,7,7,7...], upper bound = len(nums)

        for num in nums: 
            count[num] += 1

        for num, frequency in count.items(): 
            freq[frequency].append(num)


        sol = []

        for i in range(len(freq)-1, -1, -1): 
            for element in freq[i]: 
                sol.append(element)

                if len(sol) == k: 
                    return sol 
        