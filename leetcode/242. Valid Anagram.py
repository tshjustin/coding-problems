class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        just maintain counts of each other 

        will not use counter here since advanced applications require fine grain control 
        """
        from collections import defaultdict

        s_map = defaultdict(int)

        for char in s: 
            s_map[char] += 1

        t_map = defaultdict(int) 

        for char in t:
            t_map[char] +=1 


        return t_map == s_map

    