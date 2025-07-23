class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        """
        Traverse the array twice 

        first pass -> remove the substring with the higher point 

        second pass -> remove the remiainder 
        """

        sol = 0     
        

        if x > y: 
            first, second = "ab", "ba"
            first_val, second_val = x, y
        else: 
            first, second = "ba", "ab"
            first_val, second_val = y, x
        
        temp = []
        for char in s:
            if temp and temp[-1] + char == first:
                temp.pop()
                sol += first_val

            else: 
                temp.append(char)

        stack = []
        for char in temp:
            if stack and stack[-1] + char == second:
                stack.pop()
                sol += second_val
            else:
                stack.append(char)

        return sol