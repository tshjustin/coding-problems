class Solution:
    def maxSubArray(self, nums: List[int]) -> int:            
        res = nums[0]
        total = 0

        # greedily keep the sum > 0
        # if < 0, then reset the total 
        # start counting again 
        for n in nums:
            if total < 0:
                total = 0

            total += n
            res = max(res, total)
        
        return res