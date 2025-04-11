class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        [1, 3]
        [6, 9]

        cur 
        1--------3
                        6--------9

           2---------5
           k 

        if we encounter an overlap, that is the start of the new interval cur[0] < k[1] and cur[1] < k[0]

        1. add in new interval 
        2. sort based on the starting points 
        3. incrementally build the solution - that is to start from the first interval

        for int in intervals: 
            if int overlaps with current solo: 
                merge 
            else: 
                append 

        return sol 
        """

        intervals.append(newInterval)
        intervals.sort() # for list, automically apply on the first element of the list 

        sol = [intervals[0]]

        for i in range(1, len(intervals)): 

            # since sorted, we know that the next element would come after the current 
            # hence the only condition for overlapping if the start of next is before the end of current

            # if we do find an overlapping - merge it - which is to adopt the end point of the new interval - hence MODIFY what we currently have 

            if intervals[i][0] <= sol[-1][1]: 

                # the assumption with this is that we always choose the added one as the new - but could be false 
                # sol[-1][1] = intervals[i][1]

                # think of example 2 -> [4,8] [6, 7] => note that 7 < 8, so we may falsely put as 7
                sol[-1][1] = max(sol[-1][1], intervals[i][1])

            else: 
                sol.append(intervals[i])

        return sol 