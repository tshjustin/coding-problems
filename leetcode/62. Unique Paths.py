class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        From drawing the solution out 

        Consider a 2D table, where each grid represents the position where we can come from 

        dp[0][0] = 1, since there is only one way we can appear at the starting position 

        dp[0][1] = 1, since we can only come from the left (right movement from dp[0][0])

        dp[0][1] = ... = d[0][n-1]

        d[1][0] = 1, since we can only move from the top 

        dp[1][1] is where it gets interesting. Notice that we can either from the dp[0][0]
        start -> right -> down
        start -> down -> right 

        hence dp[1][1] = dp[1][0] + dp[0][1] 
        dp[r][c] = dp[r][c-1] + dp[r-1][c] 

        to confirm this, just draw all the possible paths for a small test case -> notice that it holds up ! 

        Essentially we are getting the number of ways to a postion from 2 possbile previous states (right) + (down), 
        similar to climbing stairs 

        There are 2 ways to solve this, either we think from it backwards where we say 
        "how many ways from ending -> the previos states" 
        "or start from dp[0][0] itself" 

        Maybe its better to start from the the back since its more align to starting from bottom up 

        BUT another way is to make the found recurrance, we is super easy to understand
        """

        dp = [[1 for _ in range(n)] for _ in range(m)]

        # now we can just start after the first row and after the first column 

        for row in range(1, m): 
            for col in range(1, n): 

                dp[row][col] = dp[row][col-1] + dp[row-1][col]

        return dp[m-1][n-1]


        """
        Another way is to work from the back

        Its basically the same, just that the recurrance just needs some tweaking 

        Another optimization is to note that we just need to maintain 1 array at a time, which is the previous row 
        but then we still need to create a state from the current row, hence override the prev row with the current row
        """