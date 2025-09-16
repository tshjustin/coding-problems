# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Since the path dont need to go through the root, 

        For each node, check the left and right path, the update the solution as we need to 


        try
        ----
        For traversal, ensure that we return 1 each time when we backtrack 
        """

        sol = [0]

        def dfs(root): 

            if not root: 
                return 0 

            left_length = dfs(root.left)
            
            right_length = dfs(root.right)

            current_diameter = left_length + right_length 

            if current_diameter > sol[0]: 
                sol[0] = current_diameter 

            return 1 + max(left_length, right_length) # since we are just wanting to find the height of the left and right of each node 

        dfs(root)
        return sol[0]

