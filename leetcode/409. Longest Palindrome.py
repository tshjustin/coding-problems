class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        1. count the number of occurances of each char 

        2. start with an odd number char in the middle - remove this one instance 

        3. if a char count % 2 : add to left and right 

        4. do until left with odd numbers / no more


        """

        # now how to traverse such that i can hit all elements 
        # how do i even pick the element that is odd ? 

        # we can try use a set that keeps track of the elements that we used 

        # in fact we can just keep track of the char in a set 
        # if a char is already inside a set , then we remove it, then +2 (add left and right)
        # if a char is inside a set, means that there's only one now. The final solution just + 1

        sol = 0
        char_set = set()

        for char in s: 

            if char in char_set: 
                char_set.remove(char)
                sol += 2

            else: 
                char_set.add(char)

        return sol + 1 if char_set else sol 