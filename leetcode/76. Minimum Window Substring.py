class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        s => len = m 

        t => len = n

        Substring t => must be found fully inside s, and must be continous BUT the characters inside may not need to be in order 


        brute_force 
        -----------
        for all character: 
            try all length 
        
        try 
        ----
        1. Use a hash_map to count the characters that we are considering inside a candidate substring 

        2. the window size has a min length of n

        3. left_pointer = 0
           right_pointer = left_pointer + n 


        The thing is that if we keep incrmeneting the right pointer, we will keep increasing our sol length 
        and there is not much indicator to move the left pointer 

        1. Left and right pointer starts at 0 
        2. Keep expanding the right pointer until we get a candidate substring 
        3. Once we get this candidate substring, see if we can shorten the substring to get a better solution -> increment left pointer 
        4. If we hit the end of the string (right hits the end), then we just increment the left pointer, hoping to get more solutions 

        """
        
        if len(s) < len(t):
            return ""

        if s == t:
            return s 

        sol_start, sol_len = 0, float('inf')
        left, right = 0, 0
        m = len(s)

        t_map = {}
        for char in t: 
            t_map[char] = t_map.get(char, 0) + 1

        window_map = {}

        while right < m: 
            
            window_map[s[right]] = window_map.get(s[right], 0) + 1

            # if we find a candidate substring , then keep incrementing the left pointer 
            # this loop would help us keep looking, and invalidates the need for anohter loop outside
            # if the right pointer is at the last element, then for some left pointer L, would keep shrinking until we break the condition 
            # hence all those windows that comes after the first invalidated one are invalids too 
            while self.is_valid_window(window_map, t_map): 

                if right - left + 1 < sol_len:

                    sol_len = right - left + 1
                    sol_start = left

                left_val = window_map[s[left]]

                if left_val - 1 <= 0: 
                    del window_map[s[left]]
                else:
                    window_map[s[left]] = left_val - 1 
                left +=1    

            right +=1 

        return "" if sol_len == float('inf') else s[sol_start:sol_start + sol_len] 

    def is_valid_window(self, window_map, t_map):
        for char, required_count in t_map.items():
            if window_map.get(char, 0) < required_count:
                return False
        return True