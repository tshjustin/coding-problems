class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        check anagram ==>
        check that the substring have the same number of char as the string given

        ab = ba since a_count_s = 1 = a_count_p 


        naive solution 
        --------------
        for all starting position of s: 
            for the string size p: 
                check anagram

        => O(n^2)


        Sliding window 
        ---------------
        window_size = length of p 

        the moment we see a violation (string mismatch), incremenet the window
        """
                
        # def count(substring, p): 
        #     """ 
        #     This check can be costly since recalcuating each time 

        #     O(window_length)

        #     But notice that if just maintain 1 table throughout and then use this 
        #     and minus and + each time , then check if equal => should be safer 

        #     """
        #     substring_map = {} 

        #     for char in substring:
        #         substring_map[char] = substring_map.get(char, 0) + 1 

        #     p_map = {}

        #     for char in p:
        #         p_map[char] = p_map.get(char, 0) + 1 


        #     return substring_map == p_map 

        # counting map of p 
        # p_map = {}
        # for char in p:
        #     p_map[char] = p_map.get(char, 0) + 1 

        # # counting map of substring
        # substring_map = {} 

        # sol = []    
        # window_length = len(p)

        # for i in range(len(s)-window_length+1):
            
        #     # if the dict is initally unpopulated 
        #     if not substring_map: 
        #         for char in s[i:i+window_length]:
        #             substring_map[char] = substring_map.get(char, 0) + 1 

        #     # perform the update -> since we sliding window, minus prev char and add the new char
        #     substring_map[s[i-1]] = substring_map.get(s[i-1], 0) - 1
        #     substring_map[s[i+window_length]] = substring_map.get(s[i+window_length], 0) + 1

        #     # do the check each time 
        #     if substring_map == p_map: 
        #         sol.append(i)

        # return sol 

        from collections import defaultdict

        if len(p) > len(s):
            return []

        p_map = defaultdict(int)
        window_map = defaultdict(int)

        for char in p:
            p_map[char] += 1

        result = []
        window_size = len(p)

        # first window ==> easier to think of the current pointer as the right boundary 
        for i in range(window_size):
            window_map[s[i]] += 1

        if window_map == p_map:
            result.append(0)

        # slide window 
        for i in range(window_size, len(s)):
            
            # rm left most char 
            left_char = s[i - window_size]
            window_map[left_char] -= 1

            # delete the entry 
            if window_map[left_char] == 0:
                del window_map[left_char]

            # add new char 
            right_char = s[i]
            window_map[right_char] += 1

            # compare maps
            if window_map == p_map:
                result.append(i - window_size + 1)

        return result