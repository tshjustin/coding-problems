class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        for each element: 

            assume first element is the maj 

            if same elemnt
                +=1 

            else 
                -=1 

            if coutn < -1 
                change element 

        """
        maj, count = nums[0], 1

        for i in range(1, len(nums)): 

            if nums[i] == maj: 
                count += 1

            else: 
                count -= 1

            if count < 0: 
                maj = nums[i]
                count = 1 

        return maj
        