class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        """
        Drawing it out literally views the solution space 

        The next problem is knowing how to find the closest non-equal neighbour left and right of the current element 

        Brute force 
        ------------
        For an element: 
            check left until find non-equal ==> but actually we just need to check the next element since we skip out the dups 
            check right until find non-equal 

        maintain a traversing pointer that counts our solution , that skips the first and last element since they are always not counted 

        Appraoch
        ---------
        1. If we encounter a duplicate, just traverse until we get the last element of the duplicate rows 

        2 2 2 1 ===> 2 2 2 1, since its the exact same that if we count via the first or last element of the duplicate nums 
        ^                ^ 

        2. Now the tricky part is such that our left pointer must maintain at the element before the rows of duplciates, 
        this can be done with just only updating the left pointer when nums[i] != nums[i+1]
        """

        sol = 0 
        left = 0 
        
        for i in range(1, len(nums) - 1): 
            
            # keep skipping until the next element is not equal 
            if nums[i] != nums[i+1]:
                
                # check for the hill and valley 
                if (nums[i] > nums[left] and nums[i] > nums[i+1]) or (nums[i] < nums[left] and nums[i] < nums[i+1]):
                    sol +=1 

                left = i # such that we can skip the duplicates 

        return sol 



