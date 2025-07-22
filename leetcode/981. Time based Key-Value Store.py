class TimeMap:

    def __init__(self):
        self.key_map = {} # {key: [(timstamp, value)]} ==> for the same key, there are multiple assoictiated timestamps with values, that are sorted
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        """
        We want to ensure that the key_map is in increasing order 
        """
        if key not in self.key_map:
            self.key_map[key] = [] 

        self.key_map[key].append((timestamp, value)) # alr sorted 

    def get(self, key: str, timestamp: int) -> str:
        """ 
        Given a key and timestamp, would return the assoiciated value with a timestamp that is smaller and closest to the given timestamp 
        """
        if key not in self.key_map: 
            return ""

        best_match = -1 

        # we can just do a binary search here to get the solution [(1, a), (2, b), (3, c), (6, d), (7, e)]
        # but note that we we must account if the tiemstamp is not actually there 
        # thus just take the prev best 
        left = 0
        right = len(self.key_map[key]) - 1

        while left <= right: 
            mid = (left + right) // 2
            
            best_match = mid - 1

            if self.key_map[key][mid][0] == timestamp: 
                return self.key_map[key][mid][1]

            # if our solution is greater than the middle, then we should search right 
            # also we would garantee the pick the element that is <= to current timestamp 
            # only timstamps (not the inputs) can be possible solutions 
            # hence if our input timestep is large, then we update the best_match, since its garantee (since its sorted)
            # that we would pick a smaller timestamp as the sol 
            elif timestamp > self.key_map[key][mid][0]: 
                best_match = mid
                left = mid + 1

            else:
                right = mid - 1

        return self.key_map[key][best_match][1] if best_match != -1 else ""



"""

{key:value}

Key => not unqiue but dependent on timestamp 

The timestamp is unique, hence we can store based on that 


Maybe can just do {time: {key:value}}
"""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)