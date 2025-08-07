class Solution:
    def trap(self, height: List[int]) -> int:
        """
        we want the total amount of rain water that can be trapped after raining 


        the hard part is say in the middle portion of the example: 
            how do we know how much water can be trapped in this small pond 

            height = min(left_wall, right_wall) ==> but this does not capture the divit in the middle 

            what i mean by the above ==> the bottom elevation also plays a part in the amount of water trapped inside that unit 
            
            for a unit :
                current elevation 
                left_max_height \____ take the min of these 
                right_max_height /

        1. can traverse unit by unit 
        2. determine the constraints of the elevation, left and right wall 
            a. now take a look at the first water point 
            b. it is tempting to take the height[3] as the right wall
            c. but not needed , since we can just take the same height[n-1] as the right bound, since the limiting 
                factor is still height[2]

            d. but when do we increment left and right ? We would need to take a look at the middle portion 
            e. left_wall = 2, right_wall = 3 ==> we try a greedy !
            f. each time we traverse the cur, we move the left and right, if high wall , then so be it, since limiting is still min 

        3. slowly sum up our solution 


        try 
        ----
        taking the left and right max of the ith element in the array

        but keep calculating can be costly 

        in the analysis above , if i shift  the right pointer, then when i go to an element after it, the right pointer may be on the left of the ith element 


        so the problem i have now is how to efficiently find the left and right max ? 

        again 
        -----
        for the current element, we are limited by the min of the left and right 

        not just any left or right, but by the max left / right that we have seen 

        instead of calculating sequtnailly, how abot making use of the above logic, and cacluating water left and right until we interset ? 
        
        """
        # sol = 0 

        # n = len(height)

        # left, right, cur = 0, n-1, 0 

        # # keep track of the max height that we see --> allows to to know our boundaries 
        # # since we know which side has the minimum max height, we increment the opposite 
        # # say left=1 and right = 3, then we would move left since this is the limitation 
        # left_max = height[left]
        # right_max = height[right]

        # # the first and last height cant hold any water 

        # for i in range(1, n-1): 
            
        #     current_unit_water = min(left_max, right_max) - height[i]

        #     sol += current_unit_water if current_unit_water > 0 else 0 

        
        # return sol 

        sol = 0 
        n = len(height)
        left, right = 0, n-1 

        left_max = height[left]
        right_max = height[right]

        while left < right: 

            # we are limited by the minimum of the max height: 
            if left_max < right_max: 
                min_height = left_max 
                left +=1 # increment the left, since we know its the limiting, we try to find a higher one 

                left_max = max(left_max, height[left])
                
                current_unit_water = min_height - height[left]
                sol += current_unit_water if current_unit_water > 0 else 0 


            else:
                min_height = right_max 
                right -= 1
                right_max = max(right_max, height[right])

                current_unit_water = min_height - height[right]
                sol += current_unit_water if current_unit_water > 0 else 0 


        return sol 





        