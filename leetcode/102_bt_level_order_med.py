# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        perform bfs - but key is to take the # of child of that level -> level_size 

        enquque node 
        """
        from queue import Queue

        if not root: 
            return [] 
        sol = []

        q = Queue()

        q.put(root)
        
        while not q.empty():
            
            # take the level size before appending the childrens 
            level_size = q.qsize()
            cur_level = []

            for _ in range(level_size): 

                current_node = q.get()

                if current_node.left: 
                    q.put(current_node.left)
                
                if current_node.right: 
                    q.put(current_node.right)

                cur_level.append(current_node.val)
            
            sol.append(cur_level)

        return sol 