class Solution:
    """
    string1;string2;string3... .

    but this would be bad 

    stringf_length;string_length...

    try
    ---
    len1#string...len2#len3...
    """
    def encode(self, strs: List[str]) -> str:
        res = ""

        for string in strs:
            res += str(len(string)) + "#" + string  # O(m) operation 

        return res 


    def decode(self, s: str) -> List[str]:
        
        sol = []
        i=0

        while i < len(s):
            j = i 

            while s[j] != '#':
                j +=1 

            word_length = int(s[i:j])
            word_start_idx = j + 1
            word_end_idx = word_start_idx + word_length 

            sol.append(s[word_start_idx:word_end_idx])

            i = word_end_idx

        return sol 
            
                
