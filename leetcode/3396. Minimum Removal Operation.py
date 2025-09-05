class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        """ 
        cant modify the positions 

        remove, then check 

        """
        sol = 0 

        while len(nums) != 0 : 
            
            if self.unique_array(nums): 
                return sol 

            nums = nums[3:] # slow operation 
            sol += 1

        return sol 

    def unique_array(self, nums): 
        seen = set()

        for num in nums: 
            if num in seen:
                return False 

            seen.add(num)

        return True


# class Solution:
#     def minimumOperations(self, nums: List[int]) -> int:
#         """
#         from the back, if we see a duplicate element , thne 
#         can just chop the whole lot infront - more cutting 

#         i // 3 => groups of 3 infront 

#         + 1 => final group that contains the 3, which could be incomplete 
        
#         """
#         seen = [False] * 128
#         for i in range(len(nums) - 1, -1, -1):
#             if seen[nums[i]]:
#                 return i // 3 + 1
#             seen[nums[i]] = True
#         return 0