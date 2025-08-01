class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        We are given x digits , from these digits, then we take 
        1 letter from 1 digit 

        to check for mathematical correctness: 

        1st digit -> 3 options 
        2nd digit -> 3 options 
        3rd digit -> 3 options

        a b c 

        ad ae af 
        bd be bf 
        cd ce cf 

        ad -> ....


        Iterate through each element of the digit string [2, 3 ....]
        Then inside the digit 2 --> iterate through each character in the mapping



        The trick is to notice that we can use the same IDX for the letters_in_digits AND the current_length_of_string
        """

        if not digits:
            return []

        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        res = [] 

        def backtrack(combination, idx): 

            if idx == len(digits): 
                res.append(combination[:])
                return 


            for letter in digit_to_letters[digits[idx]]: 
                backtrack(combination+letter, idx+1)
        

        backtrack("", 0)
        return res 
