class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        
        try 
        -----
        1. sorting --> O(logn) run time 

        2. set --> O(n) space 

        3. slow and fast pointers 


        observe
        ---------
        1. treat the array like a linkedlist , where each array value 
        points to some index 

        2. If nums[i] = j, then that means i points to j, hence a linked list structure

        3. 1st round of fast and slow --> would point at SOME node INSIDE the cycle 

        4. now we want to find the beginning of the start of the cycle --> thats the duplicate element 

        Let A be the distance from the start of the cycle to the meeting point 
        Let B be the distance from the cycle start to the meeting point 
        Let C be the remaining distance in the cycle 

        Cycle Length = B + C

        Now we want some relation that equals the distance 

        In phase 1: 
        Slow traveled => A + B
        Fast traveled => 2 (A+B) , since twice as fast 

        Another formulation of Fast is = A + B + C + B 

        So A  = C, 

        So the pointer would travel distance A to reach cycle beginning 
        Pointer at the meeting point would travel C to reach cycle beginning

        Hence we can formulate 

        1. slow pointer reset to start 
        2. keep pointer at meeting point 
        3. move both pointer one at a time until meet 
        4. solution
        """

        slow, fast = 0, 0 

        while True: 
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast: 
                break 

        slow2 = 0
        while True: 
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                return slow 