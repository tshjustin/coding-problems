class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        the solution is an empty array 

        1. traverse the array 
        2. if the next interval come, check if there is an overlap 
        
        an overlap occurs if: 
            1. the start time of the SECOND array is BEFORE the end time of the FIRST ARRAY 
        
        3. if overlap, then merge, BUT continue to check if the current array has an overlap with the next 


        # this is on the assumption that the start times are sorted 

        """
        intervals.sort(key=lambda x: x[0])
        res = [] 
        res.append(intervals[0])

        for interval in intervals[1:]: 
            
            # if overlapping 
            if self.is_overlapping(res[-1], interval):   
                # then perform the merge 
                new_interval = [min(res[-1][0], interval[0]), max(res[-1][1], interval[1])]
                res.pop()
                res.append(new_interval)
            else: 
                res.append(interval)

        return res 
    
    def is_overlapping(self, a, b):
        """ 
        the case when NOT overlap: 

        [a0 a1]
                [b0 b1] => a1 < b0 

        [b0 b1]
                [a0, a1] => b1 < a0 

        Hence overlap => negation => ! (a1 < b0 OR b1 < a0 )

        """
        if a[1] >= b[0] and b[1] >= a[0]:
            return True 

        return False  
