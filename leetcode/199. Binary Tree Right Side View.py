# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        use a BFS 

        for each level:
            append children of that level 
            find the number of children --> len()

            pop the last element 
            append to result 
        """

        if not root: 
            return [] 

        from collections import deque 
        sol = []
        q = deque([])
        q.append(root)

        while q: 
            number_of_childs = len(q)
            
            for i in range(number_of_childs): 
                current_node = q.popleft()

                if current_node.left:
                    q.append(current_node.left)

                if current_node.right:
                    q.append(current_node.right)

                if i == number_of_childs - 1: 
                    sol.append(current_node.val)
        return sol 
        