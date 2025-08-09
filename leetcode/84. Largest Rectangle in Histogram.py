# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         """
#         The goal is to find the next largest integer, since typically the solution is either 

#         1. The width itself being the solution 
#         2. multiple histograms make up the solution 


#         We want to track the highest "height" --> want a monotonically increasing stack 

#         [2, 5, 6, ...], since this is where we would most likely get our solution 

#         why ? --> consider [2, 1, 3] ==> 1 is the limiting factor here, and if we include it, we limit all our solution to 1*(widith)

#         try 
#         ---- 
#         traverse the array and maintain a monotoncially increasing stack 

#         but now how do we find the solution ? --> need to [2,_,5,6] => [2] , [5,6]

#         another case to consider ==> [2, 1, 5, 1 , 6] ==> what if we add a tracker that tracks when was the last time we updated ? 

#         say we updated at 
#         2 => tracker = 1
#         1 => tracker = 0 (since reset, no update)
#         5 => tracker = 1
#         1 => tracker = 0
#         6 => tracker = 1 

#         Now for the example [2, 1, 5, 6]
#         2 => tracker = 1
#         1 => tracker = 0 
#         5 => tracker = 1 
#         6 => tracker = 2

#         Each time we incrmenet the tracker, we check the solution with min(..)

#         Now another case to think about [5,6,7,8]
#         sol = 5 * 4, but how do we know to maintain the min height = 5? use a tracker 

#         Now consider the case for [1, 1]
#         would need to elimintate the first check of 
#         if not stack:..., and combine with the tracking logic, since the tracker would now start from idx=0
#         """

#         stack = [] 
#         sol, tracker = 0, 0

#         for height in heights: 

#             # if we encounter a greater height than the top of the stack, then we append it
#             if not stack or height > stack[-1]: 
#                 stack.append(height)
#                 tracker +=1 

#                 if tracker > 1:  # 1
#                     min_height = min(stack[-2], height)  # this is wrong since i there might be a standalone which is greater than the min 
#                                                          # should only start tracking the height if we have CONSECUTIVE increment 
#                     sol = max(sol, min_height*tracker)

#                 sol = max(sol, height)

#             else: 
#                 tracker = 0
#         return sol 


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        1. keeps track of indices and stores increasing height 

        2. if we meet a short height, keep popping out tall heights and find all the possible solutions it can find 
           [2,1,5,6,2] ==> when hit the last 2, find the rectangles 6 , 5 can form , with the width calculation in mind 

        3. then append that height to the stack, since we want to see if there's any more possible solutions 

        4. once we reach the end heights array, try to find more solutions


        """
        stack = []  # store indices 
        max_area = 0
        
        for i, height in enumerate(heights):

            # pop from stack while current height is less than stack top
            while stack and heights[stack[-1]] > height:
                h = heights[stack.pop()]

                # if stack empty, width is i, else i - stack[-1] - 1
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * width)
            
            stack.append(i)
        
        while stack: # garanteed increasing array, in sequence 
            h = heights[stack.pop()] # stack.pop() ==> indices, h => gets the height 
            width = len(heights) if not stack else len(heights) - stack[-1] - 1
            max_area = max(max_area, h * width)
        
        return max_area