class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Some observations 

        1. Each row is sorted --> Perform binary search row wise 

        For each row: 
            perfrom binary search --> log(n), where n is the number of rows 


        If there are m rows --> mlogn

        Note 
        -----------------
        Look at the columns --> Note that its sorted downwards as well 

        This would allow us to find the best row, rather than looking at each row like before
            - To find the candidate row 
            - Look at the last element of the prev row 
            - Look at the first element of the next row 


            - How to look for good rows ???? 
                - It is not possbile to zoom in directly on the row 
                - The best we can do is to check the first element of the row 
                - If this first element is larger than the target, then cfm we dont search here 
                - And we dont have to search anything that comes after it! ==> right = middle - 1
                - Else we just slowly increment the left pointer by 1 , since possible candidates 

        Then we use BS again in that candidate row 
        """

        # def bs(arr):
        #     left, right = 0, len(arr) -1 

        #     while left <= right: 
                
        #         middle = (left + right) // 2
        #         middle_val = arr[middle]

        #         if middle_val == target: 
        #             return True 

        #         elif middle_val > target: 
        #             right = middle - 1

        #         else: 
        #             left = middle + 1

        #     return False 


        # rows = len(matrix)
        # cols = len(matrix[0])

        # left_col, right_col = 0, rows - 1 # for finding candidate rows 

        # while left_col <= right_col: 

        #     middle_col = (left_col + right_col) // 2
        #     candidate_start_val = matrix[middle_col][0]

        #     if candidate_start_val == target:
        #         return True 

        #     # the candidate must have a value SMALLER than the target 
        #     # Then this row would be an ideal candidate 
        #     elif candidate_start_val < target: 

        #         # try BS here on that row 
        #         if bs(matrix[middle_col]):
        #             return True 

        #         left_col = middle_col + 1

        #     # If the candidate_start_val is large, then this row is NOT a candidate
        #     # Hence we search lower 
        #     else: 
        #         right_col = middle_col - 1

        # return False 
        """
        Another observation one can make is sort of a stair case search 

        1. Start at the top right corner 

        2. If the value is larger than target --> then we would go left to get smaller value 

        3. If the value is smaller than target --> then we go down to get larger 
        """

        row = 0 
        col = len(matrix[0])-1

        while 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
            
            value = matrix[row][col]

            if value == target:
                return True 

            elif value > target: 
                col -=1 

            else: 
                row += 1

        return False 









        