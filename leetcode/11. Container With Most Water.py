class Solution:
    def maxArea(self, height: List[int]) -> int:
        """ 
        The maximum volume = min(8, 7) => 7 * (idx 8 - idx 1) = 7 * 7 = 49

        1. Note the vertical height 

        2. Note the horizontaol height 


        Greedy solution 

        Try calculating when 

        1. The vertical distance is high ! 

        2. The horizontal distance is high 

        

        Brute Force 
        -----------
        For each height in the array:
            for every other height in the array:
                calculate volume

        O(n^2)


        Optimized 
        -----------
        Use a left and right pointer 

        calculate volume 

        We want to greedily go for heights that are large! while traversing the array, hence horizontal dont matter as much 

        left pointer 
        ------------
        if the current height is high: 
            maintain 

        if the current height is low compared to next: 
            then +1 

        right pointer 
        -------------   
        if the current height is high: 
            maintain 

        if the current height is low comapred to next: 
            then -=1 


        Becomes a question of cases: 

        if next left is larger and next right is smaller: 
            left +=1 

        if next left is lower and next right is larger: 
            right -=1 

        if next left is higher and next right is higher: 
            left +=1, right -=1 

        if next left is lower and next right is lower:
            traverse!, such that we find next possible solutions ! 


        # hold the right 
        if right_height >= next_right_height and left_height < next_left_height: 
            left +=1 
        """


        # left, right = 0, len(height)-1
        # sol = 0 

        # while left < right: 
            
        #     current_volume = min(height[left], height[right]) * (right-left)
        #     sol = max(sol, current_volume)

        #     if height[left] < height[left+1] and height[right] >= height[right-1]: 
        #         left +=1 

        #     elif height[left] >= height[left+1] and height[right] < height[right-1]:
        #         right -=1 

        #     else: 
        #         left +=1 
        #         right -=1  

        # return sol 

        """
        note that in the greedy scenario, we want to alwyas find a taller wall 

        since water is bounded by the shorter wall , when we see one side of the wall is short, we want to search for candidiates 

        greedy dont care about looking for the next val before hand, it just moves 

        """

        
        left, right = 0, len(height)-1
        sol = 0 

        while left < right: 
            
            current_volume = min(height[left], height[right]) * (right-left)
            sol = max(sol, current_volume)

            if height[left] < height[right]: 
                left +=1 
            
            elif height[right] < height[left]: 
                right -=1 

            else: 
                left +=1 
                right -=1

        return sol 





