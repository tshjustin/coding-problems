class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        brute force 
        -----------
        sort then take the consecutive 


        o(n)
        -----------
        The elements do not have to be consecutive in the original array

        1. store in a bucket
            a. where freq[i] is the precense of an element 
            b. i = the element itself, which is increasing 

        2. then just do a scan
        """
        sol = 0 

        num_set = set(nums)

        for num in num_set:
            
            # start from the first num
            if num-1 not in num_set:
                length = 1

                # terminate only if we stop finding that consecutive element 
                while num+length in num_set: 
                    length += 1

                sol = max(sol, length)

        return sol 