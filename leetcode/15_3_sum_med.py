class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Brute force: 

        for each element 
            for each element
                for each element 
                    check set 

        
        take one single element -> becomes a 2 sum problem

        To prevent duplicates - ensure that the search only goes forward - so we dont relook back at the previos elements and thus dups 
        

        """
        # slow operation 
        # sol = [] 
        # seen = set() 

        # for idx, num in enumerate(nums): 

        #     target = -num 

        #     # now solve the 2 sum problem 
        #     hm = {}

        #     for i in range(idx+1, len(nums)):  # ensure that we start from the next element - prevent dups 

        #         new_sum = target - nums[i]

        #         # if we saw the element before 
        #         if new_sum in hm: 
        #             triplet = tuple(sorted([num, nums[i], new_sum])) # note that sort is an inplace operation, for ease of computation just use sorted

        #             if triplet not in seen: 
        #                 sol.append(list(triplet))
        #                 seen.add(triplet) # lists cant be added to set - must use tuple 

                
        #         # store the element that we have just seen 
        #         hm[nums[i]] =  i 

        # return sol

        # slow because of lookup and handling - prevent small optimzations such as skipping certain eleements that are dups 
        

        """
        sort 

        use 2 pointers
        """
        sol = []
        nums.sort()
        n = len(nums) - 1

        for idx, num in enumerate(nums): 
            
            # so that we dont have to repeat the same for the first element that appears as duplicates -> [-1, -1, -1] => just skip to the last -1 
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue 

            # this is an early temrination since 3 positive wont make a 0 - hence just check the first number (sorted behavior!)
            if num > 0:
                break 

            target = -num 

            left, right = idx+1, n

            while left < right: 

                cur = nums[left] + nums[right]

                if cur == target: 
                    sol.append([num, nums[left], nums[right]])

                    # we can optimize here - since we can just skip all the duplicates at once 

                    while left < right and nums[left] == nums[left+1]:
                        left +=1 

                    while left < right and nums[right-1] == nums[right]:
                        right -=1 
                    
                    # finally push it down to the next non-same element 
                    left += 1
                    right -= 1

                # we are overshooting, hence we should go for smaller number 
                elif cur > target: 
                    right -= 1

                else: 
                    left +=1

        return sol 

        