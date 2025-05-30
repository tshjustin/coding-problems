class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Maintain 2 arrays

        left = [] 

        right = [] 

        sol = []

        where left, right are the product of the array, except the self 

        if self = i, then 

        left[i] = left[1] * left[2] * ... * left[i-1]
        right[i] = right[i-1] * left[i-2] * ... * left[n]

        sol[i] = left[i] * right[i]

        left[2] = left[1] * nums[1], since left[i] is the left of nums[1]
        left[i] = left[i-1] * nums[i-1] 
        """


        n = len(nums)

        left, right, sol = [1] * n, [1] * n, [1] * n
        
        # skip first 
        for i in range(1, n): 
            left[i] = left[i-1] * nums[i-1]
        
        # skip last - 0 indexed 
        for i in range(n-2, -1, -1): 
            right[i] = right[i+1] * nums[i+1]

        for i in range(n): 
            sol[i] = left[i] * right[i]

        return sol