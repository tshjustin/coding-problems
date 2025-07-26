class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Brute force solution 

        stack = []
        For char in string: 
            stack.append()
            "".join()
            check if word in word dict 

        ## But note that it fails for the case 
        s = "aaaaaaa"
        wd = ["aaa", "aaaa"]

        a
        aa
        aaa -> clear 
        a
        aa
        aaa -> clear 
        a -> remainder ! 

        # greedy would not work 

        1. Must remember what are some splits that we have tried 
        """
        # stack = []

        # for char in s: 
        #     stack.append(char)
        #     cur = "".join(stack)

        #     if cur in wordDict: 
        #         stack = []

        # return True if len(stack) == 0 else False 

        dp = [False] * (len(s) + 1) # 1 = basecase 
        dp[len(s)] = True # very last is true 

        for i in range(len(s)-1, -1, -1): # start from the back 
            for w in wordDict: 
                
                # check if starting from i, the string have enough char to support the operation 
                if (i + len(w)) <= len(s) and s[i:i+len(w)] == w: # check if enough words and the same word 
                    dp[i] = dp[i + len(w)] # we can word break ! 

                if dp[i]:
                    break # since we can find one word to word break it ! 


        return dp[0]

