class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        THe naive but not possible solution is to make a decision tree, 
        where we choose enumerate all coins at each node. But this would lead to duplicates [2, 2, 3] <=> [2, 3, 2]

        Another way to frame this question to get all the possible combination is to say 
        "At each node, if i pick X, then the RHS would NOT pick X ever again"

        This would garantee us not having duplicates. 


        Now, what are the items we need to track ? 

        1. current sum => to check if we exploded  
        2. current index => to see which number to add 
        3. cur ==> to see what elements we have already track! => recall that we at each stage, we have eg [2, 2, 3]
        """
        result = []
        def dfs(i, cur, total): 

            # base cases 
            if total == target:
                result.append(cur.copy()) # we use copy since we are going to use this current array to track items 
                return 

            # if we have no more candidates 
            if i >= len(candidates) or total > target:
                return 

            cur.append(candidates[i])

            # Now we make a choice --> should we include this value or not ??? 
            dfs(i, cur, total + candidates[i])

            # the other decision is if we do NOT incldue the current candidate 
            cur.pop()
            dfs(i+1, cur, total)

            # This is super important --> since we are making a exploration, to visit both sides, we are performing the above 2 calls 
            # one is to visit the left node , the other is to viist the right node 
        cur = []
        dfs(0, cur, 0)    
        return result 
        