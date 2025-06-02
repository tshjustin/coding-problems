class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Sliding window approach: 

        for char in s: 
            if window has no duplicates (maintain a seen set): 
                increment the window 
                length +=1 


            else if duplicate found: 
                shorten the window by moving the left pointer until the duplcaite is gone 
            
            # if the window rushes to the right pointer, then it could rsult in some solutions being lost 



        """

        seen = set() 
        sol = 0 # minimum sol 

        left, right = 0, 0


        while right < len(s): 

            if s[right] not in seen: 
                seen.add(s[right])
                right += 1


            # if we see that s[right] in the set, then we want to get rid of it - but wwhere is it ? keep a loop until we remove
            else: 
                while s[right] in seen: 
                    seen.remove(s[left])
                    left +=1 

            sol = max(sol, len(s[left:right]))

        return sol 