class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        a palindrone can exist anywhere inside the string 

        its a DP problem, where we notice that each character of the string can be treated as a base case 

        starting from each character, we then add in the left and right char, hence its a O(1), check since
        we just check the left and right character 

        Note that we want to return the solution, rather than just checking the length of the solution 

        we can maintain a 1D DP table, where each entry represents the length of the longest palindrone where that index is te 
        middle character of the palindrome --> actually thinking back this is wrong ? ==> in fact dont need DP table 

        for each chracter in string: 
            treat it as the center 
            expand left and right 

            if left == right: 
                length +=1 
                sol = ... if max... 

        sol 
        """

        sol = ""
        max_len = 0 
        n = len(s)

        # for i in range(1, n-1): 
            
        #     cur_len = 0 
        #     left = i-1
        #     right = i+1

        #     # there can be the case of c b b d, this hence must account for either current==left or current==right
        #     if s[i] == s[left] or s[i] == s[right]: 
        #         cur_len += 1
        #         if cur_len > max_length:
        #             max_length = max(cur_len, max_length)
        #             sol = s[left:i+1] if s[i] == s[left] else s[i:right+1]

        #     elif s[left] != s[right]: 
        #         sol = s[i]

        #     # now we repeatedly check if the left and right char are the same 
        #     elif s[left] == s[right]:
        #         while s[left] == s[right]: 
        #             cur_len += 1

        #             if cur_len > max_length:
        #                 max_length = max(cur_len, max_length)
        #                 sol = s[left:right+1]

        #             left -= 1 
        #             right += 1
        # return sol 

        for i in range(n): 

            # check for the case of odd-length 
            left, right = i, i

            # perform the expansion from the center 
            while left >= 0 and right < n and s[left] == s[right]:
                current_len = right - left + 1
                if current_len > max_len:
                    max_len = current_len
                    start = left
                left -= 1
                right += 1

            # now check for the case of even-length 
            left, right = i, i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                current_len = right - left + 1
                if current_len > max_len:
                    max_len = current_len
                    start = left
                left -= 1
                right += 1

        return s[start:start + max_len]
        
        """
        In the case of DP, we can make use of palindromes that we have already found 

        This would be a 2D DP case since we need to find the longest palindrome in the form s[i:j], thus
        need to have 2 variables 

        dp[i:j] => is s[i:j] a palindrome ? is the question that we would ask, thus each entry is a False at first 

        # from the building of the table, note that we just want upper triangle 
        # since i >= j 

        # but how we do get the solution ? 
        1. when building the base case of string len =1, len = 1
        2. when building the second base casse of string len = 2, len = 2
        3. now when len > 3, need to notice the diagonal relaationship 
        """

        # handle the building first
        max_len = 1
        start = 0 
        n = len(s)

        dp = [[False for _ in range(n)] for _ in range(n)] # +1 since we need 0,...n

        # now we start with the base cases, where we consider single strings => all palindromes 
        for i in range(n): 
            dp[i][i] = True 

        # Check for palindromes of length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                max_len = 2

        # now notice that as we build the diagonal of base case = 1, it is the middle diagonal 
        # for base case = 2, we build directly above the previous diagnoal 
        # now for the case of len>3, we build again directly above the prev diagnoal 
        # to ensure that we correctrly build our solution, we would need to traverse this table correctly, so 
        # this would define our 2 ranges 

        # note that we want to check for varying length here, in this case length = 1, hence length=n+1 ==> whole string n+1
        for length in range(3, n+1): 
            for i in range(n-length+1): # note that its hard to notice this relationship, but this is the one that gives us the i 
                """ 
                The idea behind this ranges is that: 

                1. we wnat length cause its the length of the string we want to consider 
                2. for i, just think about it, we want to start from 0, 1, 2 ... ==> s[0:j], s[1:j]...
                3. and since we want a length say=3, then obviosuly j-i must = 3 ==> s[0:4] => length=3, hence the relationship
                """
                j = i + length - 1 

                # now the DP update step, quite easy to see since the current palindrome 
                # is dependent on the previous palindrone, except its sides shaved

                if s[i] == s[j] and dp[i+1][j-1]: 
                    dp[i][j] = True 

                    # only perform the update iff we have found a palindrome 
                    if length > max_len:
                        start = i
                        max_len = length

        return s[start:start+max_len]

