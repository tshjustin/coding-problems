class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        parse 
        -------
        1. Each hour can choose a piles[i] to eat 

        2. we determine what is K 

        3. We want to find the lowest bound to eat all the bananas,
        while maintaining under the time limit 

        Observations
        ------------
        1. h is alwasy >= len(piles) , since only 1 pile at a time 
        2. upperbound = len(piles)
        3. really maximum bound = max(piles) --> if can finish this, then can finish all under h 

        Brute Force 
        ------------
        1. Try for each value [1..max(pile[i])]
        2. Iterate through each pile, and check if pile[i] / k < h
        3. track the minimum 

        Optimized
        ------------
        1. Rather than iterating through all the hours 
        2. Can we find perform a binary search on the hours instead 
        3. Since we know the bounds are 1 to max(pile[i])

        4. Then we perfrom BS to find the minimum time 

        5. Minimum time --> max[pile] // minmum time < h

        The real problem is how to check that we are within h hours: 
        Can we finish all piles with k speed and h hours ? 

        --> try a brute force check 


        finalized
        ----------
        1. Rather than going through each eating speed, which we know is bounded 
        from [1, max_number_in_a_pile], use a binary search approach 

        2. With this k, check that we can finish all the piles within k 

        3. If we can, then we should hvae found this k   
        """

        from math import ceil 

        def can_finish(k): 
            total_hours = 0 

            for pile in piles: 

                total_hours += ceil(pile/k)

                # Cant finish with this eating speed --> too long 
                if total_hours > h: 
                    return False    

            return True 

        sol = float('inf')
        left = 1
        right = max(piles) 

        while left <= right: 

            k = (left + right) // 2


            time_taken = can_finish(k)

            # If we can finish with this k, this k could be big 
            # hence we need to lower the search time, find a tigher bound 
            if can_finish(k):
                sol = min(sol, k) # Actually we can ignore this since the bound would keep getting lower and lower --> so just need a direct update | return left 
                right = k - 1

            # we are eating too slow --> so we should eat faster 
            else: 
                left = k + 1 

        return sol 




        