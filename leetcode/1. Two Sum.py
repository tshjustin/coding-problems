class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        use a hashmap that tracks the nums elements

        see if we have visited it 
        """

        hash_map = {} 

        for idx, num in enumerate(nums): 
            
            complement = target - num 

            if complement not in hash_map: 
                hash_map[num] = idx

            else: 
                return [hash_map[complement], idx]
        