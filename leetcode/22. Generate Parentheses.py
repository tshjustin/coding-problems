class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Draw a decison tree 

        Each time we can either add in ( OR )

        1. But we can only in ) iff there are more ( than )

        2. We also stop when ( or ) == 3 respectively OR 2n 
        """

        sol = []
        stack = [] # mutable 


        def dfs(open_count, close_count): 

            # base cases 
            if open_count == close_count == n:
                sol.append("".join(stack))
                return 

            # explore the path where we add (
            if open_count < n:
                stack.append("(")
                dfs(open_count+1, close_count)
                stack.pop() 

            if close_count < open_count: 
                stack.append(")")
                dfs(open_count, close_count+1)
                stack.pop() # keep popping until 

        dfs(0,0)
        return sol 


            
        