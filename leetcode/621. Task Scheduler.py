class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        1. sort based on inputs

        2. Traverse the next element ? 

        note that for the above , would need alot of interweaving 

        One key observation is to note that we would eventually have a cycle that repeats, until one of that element runs out 

        1. how do we find that cycle ? 
        
        try 
        ----
        1. find one candidate 
        2. find another element to fill the interval count, else idle 
        3. check if we form that cycle 

        4. count all the elements 
        5. while can form that cycle --> repeat until runs out 
        6. repeat the top 

        7. count the total string length


        greedy
        ------
        1. note the most frequent tasks, try to finish it as fast as possbile 
        
        2. if cooling_period=1, then A -> B -> A, B is considred the "1" here, to fill the spot 

        3. if n==0, then we can just keep filling 

        4. n => determines the size of the queue 


        1. count all the elements and store 
        2. init queue with size = n + 1
        3. take an element from the most populated array, then the next element from the next most populated array, 
        4. note the same since 

        --------
        heap => track the tasks to clear 
        time_queue => track the time for a task to be clear again --> task A at t=0 ==> task A at t=n+1

        at each time step: 
            pick tasks with greatest frequency
            
            if not in time_queue: 
                schedule it 
                add to time_queue

            else:
                idle time 

            time +=1 
        """
        import heapq
        from collections import deque

        tasks_map = {}
        for task in tasks: 
            tasks_map[task] = tasks_map.get(task, 0) + 1

        # max heap of tasks 
        heap = [(-freq) for freq in tasks_map.values()]
        heapq.heapify(heap)

        # time queue 
        # but note that there are 2 ways to check the cooldown_time
        # 1. decrement each task and its time which is tedious
        # 2. hold the absolute time, since we are in an iteration, we check the time ==> compare this absolute time with the cool_down_time, which is also absolute
        time_queue = deque([]) # i would suggest this hold (cool_down, task) --> just use a regular queue since we WONT have a case of shorter cooldown time behind

        current_time = 0 

        while heap or time_queue: 
            
            # move tasks from cooldown back to heap
            while time_queue and time_queue[0][0] <= current_time: 
                
                ready_time, current_freq = time_queue.popleft()
                if current_freq > 0 : 
                    heapq.heappush(heap, -current_freq)

            # schedule tasks if available 
            if heap: 
                current_freq = -heapq.heappop(heap)

                if current_freq > 1: 
                    ready_time = current_time + n + 1 
                    time_queue.append((ready_time, current_freq-1)) 

            current_time +=1 

        return current_time 

        
        