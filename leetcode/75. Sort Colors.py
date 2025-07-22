class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        low = boundry 0 / 1 
        mid = current element 
        high = boundry 1 / 2

        while mid <= high (since we are traversing)

        if 0: 
            swap(nums[low], nums[mid])
            increment low 
            increment mid 
            # since we know its small 

        elif 1: 
            # recall that low is the boundary of 0 and 1, thus gives us some sort of boundary to swap 
            just incremnet mid  


        else: 
            swap(nums[mid], nums[high]) ==> push high element to the right
            decrement high 
            do not increment mid since a large element (1) or even (2) may be at the end of the array (that got swapped)


        since low ==> boundary of 0 / 1, if we encounter 0 => swap 
        if 1 => just increment 
        if 2 => swap with the upper boundary 
        """

        low, mid, high = 0, 0, len(nums) - 1 

        while mid <= high: 

            if nums[mid] == 0: 
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

            elif nums[mid] == 1:
                mid += 1

            else: 
                nums[mid], nums[high] = nums[high], nums[mid]
                high -=1 