class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        Essentially find all permutation, and then the permutation with the min height 

        But we are limited by the number of edges we have --> since we are given only a certain set of edges, we
        can only form some permutations 


        observations 
        -------------
        1. The root node being in the center seems the best apporach, then connect all to them 

        a. nodes at the middle are closest to the furthest ends => This links to diameter of a tree, since its the longest distance between any 2 nodes 
        => height of root is at least half the diameter 

        -> diameter DONT have to pass through the root => "span" of the tree  ==> node with the most connection is good ! 

        2.  at most 2 centeres (either one node when odd and 2 nodes when even)
        
        sol 
        --------
        we are given the degress of each leaf => since we have edges 
        hence we know how "good" each leaf is

        1. edges given to use but not the actual graph 
        2. we want to find nodes that wehn choosen as roots gives us min height 
        
        3. from the above, nodes that are far from the "root" are bad, since they are far from center 
        4. keep removing the worse choices and we would haev the candidates 

        brute force
        -----
        for each node
            try them as a candidate 
            form tree for all of them
            track MHT 


        we want to return root labels
        """ 
        if n == 1:
            return [0] # base case if only 1 node 

        if n == 2: 
            return [0, 1] # either 0-1 or 1-0, where 0/1 are the roots 

        # build adjecncy list and count # degrees 

        # adj_list => {node: [connected_lists]}
        from collections import defaultdict 

        adj_list = defaultdict(list)
        degrees = [0 for _ in range(n)]

        for edge in edges: 
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
            degrees[edge[0]] += 1
            degrees[edge[1]] +=1 

        
        # now that we have the edge list and the degree count 
        # we want to remove edges that have LOW degree count 
        # we start from the edges, then remove the connections ==> similar to topo, but different in the sense that we dont work with DAG and edges with non-0 count

        from collections import deque

        leaves = deque([])

        for node_id, degree in enumerate(degrees): 
            if degree == 1: 
                leaves.append(node_id)

        remaining_nodes = n 

        while remaining_nodes > 2: 

            # now that we have built the queue
            # the hard thing is to know what to do with it LOL 
            # we want to remove these leaves, then find what are the next leves to remove --> similar to BFS 
            level_size = len(leaves)
            remaining_nodes -= level_size 

            # remove these leaves 
            for i in range(level_size): 
                current_node = leaves.popleft() 

                # remove this node, and the connection it has via the degree 
                # note that to remove the connections , we must 
                # 1. traverse all the neightbours of it 
                # 2. minus the degrees
                for neighbour in adj_list[current_node]: # gives us each neighbour 
                    degrees[neighbour] -=1 
                    
                    # search for new candidates too ! 
                    if degrees[neighbour] == 1: 
                        leaves.append(neighbour)
        
        # we will reach here when we are left with good candidates
        # the queue would contain "healthy" nodes, since they are remainder 
        # result = []

        # while leaves: 
        #     result.append(leaves.popleft())

        # return result
        return list(leaves)
