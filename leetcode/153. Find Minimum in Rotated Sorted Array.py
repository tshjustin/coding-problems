class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Observation 
        --------------
        1. Observe that there are 2 sorted portions 
        
        2. When we find the middle element --> we want to find if this element belongs 
        to which sorted portion 

        3. If the middle element belongs to the left portion, that means that it should be its something like 
        [3,4,5...]
        
        4. Else it would be like [6,1,2,3,4,5]

        5. Now, what is the check that we should be doing ? 

        If middle value > most left:
            This means that that the we have a left + middle 
            search left 

        else: 
            this menas that middle belongs to the right 
            search right 

        NOTE: 
        the key idea is that we dont say the first 3 elements are in left sorted, and the next 3 are in right sorted 

        ITS DYANMIC ! --> 1 element could be in the left sorted , and 9 elemnts be in the right sorted 

        We dont actually know what elements are inside each sorted portion, but we can say "GIVEN THE MIDDLE, THIS BELONGS TO WHICH SORTED PORTION"

        And we can easily see this by comparing with the most left element, since after rotation, it COULD be the smallest of the left portion array --> since 
       
        test cases 
        -----------
        4 5 0 1 2 3 
        middle = 0 
        left = 4 
        since middle < left --> we are in the right portion of the array --> search left array - NOTE THAT IN THIS CASE, ITS SPECIAL SINCE THE MIDDLE ELEMENT ITSELF IS THE SOLUTION

        3 4 5 6 1 2
        middle = 5 
        left = 3 
        5 >= 3 --> middle > left 
        a. we are in the left poriton of the array 
        b. the left portion is always going to have values that are greater than the right portion --> due to rotation
        c. search right 
        """ 
        res = nums[0]
        left, right = 0, len(nums) - 1
        
        while left <= right: 

            # find the solution --> we are in a sorted array 
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                return res 

            middle = (left + right) // 2
            middle_val = nums[middle]
            res = min(res, middle_val) # handles the case where the middle is the solution itself 

            # we are in the left portion of the array -- search right 
            if middle_val >= nums[left]: 
                left = middle + 1

            else:
                right = middle - 1

        return res 
        