class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        s1 must be a substring in s2 

        But the way it can exist in s2 is of any permutation --> just use a count 

        1. find window length -- fixed 
        2. Traverse the s2 string with that length, continuously increasing and decreasing 
        the elements 
        3. keep checking if its the same 
        """

        from collections import defaultdict 

        s1_map = defaultdict(int)
        s2_map = defaultdict(int)

        for char in s1: 
            s1_map[char] += 1

        window_length = len(s1)

        for char in s2[:window_length]:
            s2_map[char] += 1

        for right in range(window_length, len(s2)): 

            if s1_map == s2_map:
                return True 


            left_char = s2[right - window_length]
            s2_map[left_char] -= 1
            if s2_map[left_char] == 0: # note that the 0 counts were messing things up --> 0 count would make the array unequal 
                del s2_map[left_char]

            s2_map[s2[right]] += 1

        return s1_map == s2_map

            



        