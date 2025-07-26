class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        just need to return the T/F 

        A sum can only be divisble if even

        BUt if a sum is even, does not mean can be partitioned => [1, 2, 5]


        """
        total = sum(nums)
        
        if total % 2 == 1:
            return False 

        # now that we have an even sum: 
        target = total // 2

        # similar to a knapsack problem
        # each item is a 0/1 item , target = k 

        """
        track what elements we currently are taking 

        track the total sum we currently have 

           | 0 1 2 3 4 5 6 7 8 9 10 11
        --------------------------------------
        0  | T F F F F F F F F F F  F # base cases  
        1  | T T
        5  | T
        11 | T
        5  | T
           | # base cases 

        At each cell dp[i][j], we ask if we can make the current sum => j using the first i elements 
        dp[0][0] = True 
        # add 0 in the first row since it represents if no items are being used 

        dp[1][1] => Can we make the target=1 given just 1 item, which has the value 1? 
        So which direction do we come from ? => what is the recurrance relationship ? 

        dp[0][j] => Can we make a target of j given 0 items ? 
        dp[1][j] => can we make a target of j given 1 items ? 
        Since we can only either pick or dont pick an element, 

        say we choose to take the item with value 1, then we would then look at the previous row, with the target = j - current item value = 2 - 1 = 1
        hence take a look at dp[0][1] => which is False, thus current box would be False! 

        So the recurrance relation is dp[i][j] = dp[i-1][j-nums[i-1]]

        if we DONT pick the item, then we literally just copy from above us! dp[i][j] = dp[i-1][j]

        so how do we decide to pick the item or not ? 
        We ask the question, do we include the current item inside or not ? 

        If we are going to exceed, then dont take, else take --> rather straightforward 
        """
        # dp = [[False for _ in range(target+1)] for _ in range(len(nums)+1)] # inner is col, outer is rows 

        # for i in range(len(nums)+1):
        #     dp[i][0] = True

        # # now start the DP 

        # for row in range(1, len(dp)): 
        #     for col in range(1, len(dp[0])): 

        #         # if the current item is lesser than the target, then we have a choice to pick it 
        #         # but that doesnt mean we may pick it 
        #         # Hence to pick or not to pick comes down to 2 choices =>
        #         # if we pick, did we come from some state that allows us to form our sum ALONGSIDE the newly picked item ? 
        #         # if we dont pick, did we come from some state that allows to form our sum till current still ? 
        #         # hence the OR!, note that the if condition here is not about whether to pick the item or not, it just gives us a choice to pick
        #         # the actual picking is done, subjected by availability ! 
        #         if col >= nums[row-1]: 
        #             dp[row][col] = dp[row-1][col-nums[row-1]] or dp[row-1][col]

        #         else: 
        #             dp[row][col] = dp[row-1][col]

        # return dp[len(nums)][target]

        dp = [False for _ in range(target+1)]
        dp[0] = True
        
        # for each possibility 
        for num in nums: 
            for j in range(target, num-1, -1): 
                
                # we can only current the current sum, if the number we are about to pick 
                # is smaller than the sum we are required to make
                # alternatively, only check the until the number that we are considering 
                dp[j] = dp[j] or dp[j-num]
        return dp[target]

        """
        Each cell dp[i][j] only depends on:

        dp[i-1][j] (directly above)
        dp[i-1][j-nums[i-1]] (above and to the left)

        We only need the previous row to compute the current row!

        dp[j] = can we make sum j ?
        dp[0] = True since having a sum 0 is true for all cases 

        # But why iterate backwards ? 

        target = 11 
        dp = [False] * 12, to account for the first sum=0

        # Consider the case where we go forward, hence 
        d[0] = True 
        dp[1] = Can we make the sum=1? Yes, since nums=1, dp[1] = dp[1] or dp[0] (The recurrance relation)

        # before we explore the case of going forward, we ask why we have this recurrance relationship ? 

        dp[j] = Can we make the sum j. Note that we would iterate through each num,

        for num in nums: # why ? => building our solution, given the numbers we have seen so far, what is the sum we can make ==> DP, since we are starting with a small subsets of coins 
            for ... 

        hence at the current dp[j], we would be considering to add the current number num. 
        Hence if we include the current num, then our sum would be dp[j-num]
            if we DONT include the current num, then we would be having the sum as the current sum dp[j] ==> dp[j] = dp[j] or dp[j-num]


        Now lets go over the case where we go forward in the loop 
        j=1: dp[1] = dp[1] OR dp[0] = False OR True = True
        j=2: dp[2] = dp[2] OR dp[1] = False OR True = True ← PROBLEM!

        We just set dp[1] = True in this same loop iteration. 
        But dp[1] = True means "we can make sum 1 using number 1". 
        Now we're using that to set dp[2] = True, which means "we can make sum 2". 

        But to make sum 2, we'd need to use the number 1 TWICE (1+1=2). We only have one copy of number 1, hence we repeated our value.

        # but how does going backward solve this ? 
        We only use results from the previous iteration, which means each number is counted exactly once.
        """
