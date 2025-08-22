class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Monotonic stack -- Increasing 

        1. The stack would have elements that are always increasing 

        2. If there is an element that we add that violates , then we pop until 
        when we add this new element, the property is maintained 

        3. But how does it allow for the next smallest / greatest element ? 

        Say we have 

        [A, B] and that A < B , then A cant be the next greatest element of B, 
        or anything that comes before A

        4. Back to 2., note that we only start popping when we violate this property, hence 
        this means we only pop when we found an element that is smaller than the last element of 
        the stack (in the case of increasing monotonic stack)

        5. Hence this implies the following : We have found a next element that is smaller than the 
        element at that top of the stack.


        In this question, we need to find the next highest temperature: 

        1. For each element, we need to find the next greatest element 

        2. Hence we track a monotonic decreasing stack --> we only pop iff we find a large element

        3. We keep popping until we maintain the property, this means that all elements that 
        we have popped are violating --> The elements that are popped are smaller than the current
        element --> This implies that these element's next greatest is the current element as well

        """

        # track indices in this case since we need the days 
        stack = [] 
        sol = [0] * len(temperatures)

        for idx, temp in enumerate(temperatures):
            
            # Check the temperature of the top of the stack 
            # Maintain the monotonic stack property --> Decreasing in this case 
            while stack and temperatures[stack[-1]] < temp: 
                day_idx = stack.pop() # remove the element from the stack 

                sol[day_idx] = idx - day_idx

            stack.append(idx)
        
        return sol 




        