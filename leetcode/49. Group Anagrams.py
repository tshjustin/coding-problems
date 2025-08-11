class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """ 
        maintain a hash_map of 

        {arr_freq: [anagrams]}

        """
        from collections import defaultdict 

        hash_map = defaultdict(list)

        for string in strs: 
            
            arr = [0] * 26

            for char in string: 
                arr[ord(char) - ord('a')] += 1

            # since lists cant be keys 
            hash_map[tuple(arr)].append(string)

        return list(hash_map.values())

        # sol = []
        # for val in hash_map.values():
        #     sol.extend(val) # extend would flatten the list lol 

        # return sol 

            
            
        