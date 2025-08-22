class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        Drawing the graph of distance against time sees the fleet combining 

        1. If intersect --> then that means that there is a fleet 
        2. that is distance_carx == distance_cary == fleetx, and speed = min(car_x, car_y)


        Brute Force Solution
        --------------------
        1. Find all the distance of all the cars 
        2. Then match the numbers 
        3. Count the fleets
        

        Observations
        -------------------
        1. Cars closer to the target would be the blockers 
        2. Sort by postions --> since closer would be blocking --> Hence decreasing order 
        3. Find the time taken to reach the end goal --> t1 t2 .... 
        4. If t2 < t1, this means car2 will be blocked by car1 --> fleet formed 

        5. When the fleet forms, then speed is now the min of the slowest car --> this is now the 
            limiting fleet 
        6. Check the time of the next car t3, then compare this with slowest time 
        
        NOTE that we dont have to worry about fast cars behind since there is alwasy a blocking 
        car infront, if slow and cant overtake 
        """

        # pair = [(p, s) for p, s in zip(position, speed)]
        # pair.sort(reverse=True)

        # fleet = 1

        # # Find the time taken needed for the closest car to the target to reach it 
        # prev_time = (target - pair[0][0]) / pair[0][1]

        # for i in range(1, len(pair)):
        #     curr_car = pair[i]

        #     # find the time needed for the current car 
        #     cur_time = (target - curr_car[0]) / curr_car[1]

        #     # check if this is blocked by the blocker car 
        #     # if the previus time is larger than the current time, this means prev car was slower
        #     if cur_time > prev_time: 
        #         fleet += 1
        #         prev_time = cur_time  # new slowest time 

        #     # else there is no blockage --> means the current car is EVEN slower 

        # return fleet

        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []

        for p, s in pair: 
            stack.append((target - p) / s)
            """ 
            1. each time we find the time to reach the target 

            2. If the time to reach for the current car [-1] --> is shorter than 
               the time for the prev car [-2] to reach , then that means 
               --> cur car is travelling faster 
               --> Would form a fleet
               --> Hence pop()

            3. Number of elements in the stack = number of fleet 
            """
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)