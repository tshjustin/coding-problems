"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        The problem arises from the random pointers 

        Cause of it, we cant create sequentially, since if node A random pointer points to Node C, then
        when we want to create Node A, we would need Node C to be created first

        1. Use a hashmap to store the mapping of original Nodes -> New Nodes 

        2. Then we just find some linkages 


        """
        oldToCopy = {None: None}

        cur = head

        # Real Node -> Copy Node 
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next

        cur = head

        # Then now we add the linkages 
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next

        return oldToCopy[head]










