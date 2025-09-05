"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else [] - list of pointers that are conected to the current node 
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        The given node will always be the first node with val = 1


        problems: 

        1. need to find all the references on my own -> what is conencted to what ? 

        2. build the graph with the connections using Node()

        3. Return the reference to the node after completing all things 

        # Note that we are given a reference to an existing node 
        # then we just want to make a copy of it 


        method 1: 
        1. Create the adj list with BFS => O(V+E) | Space = O(V+E)
        2. Create the graph based on it => O(V+E)

        method 2: 
        1. Create the nodes as we go along  O(V+E)


        -------------------------------------------------------------
        A neater method is to map the original node to the cloned node 

        Then we return the pointer to the cloned node 

        THe tracker serves as a solution and tracking set
        """

        if not node:
            return node 

        from queue import Queue 

        q = Queue() 
        clones = {} # original_node : cloned_node 

        q.put(node)
        clones[node] = Node(val=node.val) # cloned node 

        while not q.empty(): 
            
            # no need for q size since not doing level order stuff 
            
            cur_node = q.get() # this is the original node ! 
            current_clone = clones[cur_node] # we want to update the neighbours of this node 

            for neighbor in cur_node.neighbors: # neighbour is refernecing the orignal neighbours of the original nodes 

                # if the original neighbour is not in the tracker
                # create a clone of it !
                if neighbor not in clones: 

                    clones[neighbor] = Node(val=neighbor.val) # we must instatniate first, so that the previous node created before this can connect to this 

                    # now push it to queue so that we can process it later 
                    q.put(neighbor)

                # this must be outside such that it connects even thou the node is already tracked 
                current_clone.neighbors.append(clones[neighbor]) # note that we want to conenct clone -> clone, not clone -> original 

        return clones[node] 

# ensure that we "keep a seperation layer" of cloned and original 