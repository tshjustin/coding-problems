class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Notice that this is a DAG

        Since certain courses must come before some other, we essentially want a topological order 

        but since we want to know if its possible to find an ordering, we essentially want to see if there is a cycle 

        khan's algorithm allows us to find a cycle 


        Find all the depedencies degree of each node 

        Enqueue nodes that have no dependencies  (no incoming egdes)

        while q: 

            cur = deque 
            sol.append(cur)

            for neighbour of cur: 
                incoming egde of neighnour -=1 

                if neighnour_inc_edge == 0: 
                    enqueue

        if sol.len != number vertex:
            return false 

        return True 
        """

        # build the adjacency list - [a, b] => b->a, hence a is dependent on b
        # adj list => for this node, what does this node connect to => a:[b] => a->b 

        adj_list = {}
        incoming_edges = [0] * numCourses

        for dependent, independent in prerequisites:
            if independent not in adj_list:
                adj_list[independent] = []
            adj_list[independent].append(dependent)

            incoming_edges[dependent] += 1
            

        from queue import Queue 

        q = Queue()

        for i in range(numCourses):
            if incoming_edges[i] == 0:
                q.put(i)

        count = 0 

        while not q.empty():
            curr = q.get()
            count += 1
            
            if curr in adj_list:
                for neighbor in adj_list[curr]:

                    incoming_edges[neighbor] -= 1
                
                    if incoming_edges[neighbor] == 0:
                        q.put(neighbor)
        
        return count == numCourses