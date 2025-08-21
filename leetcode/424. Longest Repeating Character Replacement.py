class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Use a sliding window and count the number of elements we have in majority 

        As we grow the window and we see if there are violations, then we increment
        the count until we hit k. 

        If we hit K, we would start shrinking the window from the left 



        try
        ----
        1. increment the window to the right 
        2. track the most frequent element, and count if there's violations each time 
        when the right pointer points to the NOT most frequent element 
        

        But the tricky part is checking the most frequent element 

        1. Just track the current most frequent element count -- that is in the current window 
        2. When the s[right] goes to another element, then perform max(max_freq, mp[s[right]])
        """

        from collections import defaultdict

        sol = 0
        left = 0 
        n = len(s)
        freq_map = defaultdict(int)
        most_freq = 0 

        for right in range(n): 
            
            # now we track the elements that we encounter 
            freq_map[s[right]] +=1 
            most_freq = max(most_freq, freq_map[s[right]])

            # [A A B C]
            # 4 - 2 = 2 ==> violation if 2 is the limit 
            # shrink the left side until this violation is broken 
            # --> make more space for the other elements 
            """     
            This is a niche observation -->

            But notice that if we do window - most_freq_cur, would need to O(26) look up
            the most freq

            But we can infcat make the most_freq the same element, since 

            to beat the current res , we need a new max freq, we dont care for anything smaller!

            Hence, we can just leave it as the max_freq, until some larger elemenet comes along 

            This has to do with the nature of when we update our solutions
            """
            while (right - left + 1) - most_freq > k: 
                
                freq_map[s[left]] -= 1
                left +=1 
            
            sol = max(sol, right - left + 1)

        return sol 

     