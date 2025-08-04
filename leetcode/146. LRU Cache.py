class Node: 
    def __init__(self, key, value, nxt=None, prev=None): 
        self.key = key 
        self.value = value 
        self.nxt = None 
        self.prev = None 

class LRUCache:

    def __init__(self, capacity: int):
        """
        Capacity would deterimine 
        
        1. number of nodes that we can hold at a time 

        2. size of hash_map 
        """
        self.capacity = capacity
        self.hash_map = {}
        
        self.head = Node(0, 0)  # dummy head
        self.tail = Node(0, 0)  # dummy tail
        self.head.nxt = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.hash_map:
            # Move to front since it was just accessed
            current_node = self.hash_map[key]
            
            # Remove from current position
            current_node.prev.nxt = current_node.nxt
            current_node.nxt.prev = current_node.prev
            
            # Add to front
            current_node.nxt = self.head.nxt
            current_node.prev = self.head
            self.head.nxt.prev = current_node
            self.head.nxt = current_node
            
            return current_node.value
        return -1
        
    def put(self, key: int, value: int) -> None:
        
        # O(1) => can just use hash_map to check rather than the linked list 
        # if too many items then evict 
        if key not in self.hash_map and len(self.hash_map) >= self.capacity:
            """
            If there are too many nodes, then we would remove the one at the back, create a new node 
            """
            lru_node = self.tail.prev
            del self.hash_map[lru_node.key]

            # just wrap around 
            lru_node.prev.nxt = lru_node.nxt  
            lru_node.nxt.prev = lru_node.prev

            new_node = Node(key, value)
            self.hash_map[key] = new_node
            
            # Add to front
            new_node.nxt = self.head.nxt
            new_node.prev = self.head
            self.head.nxt.prev = new_node
            self.head.nxt = new_node
            

        # shift the key to the front 
        # note that also another reason we store the node in the hash map is such that we can retrieve the entire ndoe later on 
        elif key in self.hash_map: 
            current_node = self.hash_map[key]
            current_value = current_node.value

            current_node.value = value 

            # would affect 3 areas -> node_before_cur , node_after_cur, nodes_before_after_new_cur

            # now the node BEFORE we remove the current node AND AFTER => the update is linked ! 
            current_node.prev.nxt = current_node.nxt
            current_node.nxt.prev = current_node.prev

            # now fix the pointers for the newly added node that was shifted infornt 
            current_node.nxt = self.head.nxt
            current_node.prev = self.head

            # the node that would get pushed back 
            self.head.nxt.prev = current_node
            self.head.nxt = current_node

            
        else: 
            """
            For newly added nodes --> add to the front

            For a Doubly linked list => <-> NODE <->

            Note that Node.nxt is RHS ->, Node.prev is LHS <-

            RHS <- is node.nxt.prev, LHS -> is node.prev.nxt
            """
            new_node = Node(key, value) 
            self.hash_map[key] = new_node # note that the hash_map stores pointers 

            new_node.nxt = self.head.nxt # since head was initally pointing to the next 
            new_node.prev = self.head # can just be the head since we always add to the front 

            # now update the tail and the head 
            self.head.nxt.prev = new_node  # can just do tail.prev honeslty 
            self.head.nxt = new_node 


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


"""
The initialization would keep track of the number of elements that we can store 

This would implicitly mean that there is some sort of heap --> 

If we add in a new element that is NOT in the heap, then we will pop out the item that we have NOT used in a long time

But how do we track the item that we have NOT used in a long time ? a queue ? 


NOTE
=====
The problem with the above is that if heap is used ==> O(logn), but we want O(1)

O(1) ==> hash_map / arrays / linked_list 

1. get() => hash_map to track the element 
2. put() => doubly linked list => allows for O(1) insertion in both ends 

Arrays => shifting of elemnts 
Linked List => update of pointers 


"""