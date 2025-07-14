class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []

        if len(nums) == 1: 
            return [nums.copy()]


        for i in range(len(nums)): 

            first_value = nums.pop(0)

            # now recurse 
            perms = self.permute(nums)

            # handle the returned elements 
            # build the solution by adding the items that are remvoed initially 
            for perm in perms: 
                perm.append(first_value)

            result.extend(perms)

            nums.append(first_value)

        return result 
