class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        observe that: 
        1. where is the pivot 

        2. there is always 1 sorted part 
        
        To answer the first question: 
        Consider a normal sorted array [0, 1, 2]. If the middle is larger than the most left element, then 
        it must be increasing (Keeps going up steadily without breaking suddenly)

        This same logic applies to a sorted array: [2,0,1]. Since the most left is larger, then there must be some rotation (but where)?

        Consider [4,5,6,7,0,1,2,3] => 7 > 4 hence it must be increasing in the left part 

        [7,0,1,2,3,4,5,6] => 2 < 7, hence the right part is increassing 

        To answer (but where)? => Not really needed since we just need to identify which part is the increasing part 


        So what if we have identified which is the sorted part ? Now we need to find the actual solution 

        If say we note that the right part is sorted, then our new left pointer would be the mid.
        This means that we are now in a perfectly normal sorted environement and can just perform normal binary search 
        [7,0,1,2], middle=7, target=0 (That is why we even consider searching for the sorted part first)

        Now we just check the solution, but there might be a chance where the solution is not here, hence must check if the target 
        fits the bounds of the current sorted which is => nums[middle] < target <= nums[right]

        TDLR:
        1. Find sorted part. Consider a normal increasing array, 
            if the midpoint is larger than the most left,
            then all elements from the start to the middle is garanteed to be increasing. Hence left side is increasing 
            else: 
                right increasing 


        2. Now that we find a sorted part, we can perform normal BS. But need to check if the answer is even in this area in the first place/

        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # left sorted part => [5,6,7,1,2] => [5,6,7], target=5
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # right sorted part => [6,7,1,2,5] => [1,2,5], target=7
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1

        