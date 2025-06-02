# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         """
#         Treat each node as an independent node

#         FInd the max height of its left subtree 

#         FInd the max height of its right subtree
         
#         max_height = max(max_height, left+right)

#         """
#         if root is None:
#             return 0 

#         # how do i return the max diameter - that is left + right 
#         # THis operation performs an addition for the current node 
        
#         #max_height = max(max_height, self.height(root.left) + self.height(root.right))

#         # the problem with this code is that it only performs for the root node 
#         # we are not looking at the left and right sub problems! 
        
#         # this would lead to TLE 
#         diameter_through_root = self.height(root.left) + self.height(root.right)
#         diameter_left = self.diameterOfBinaryTree(root.left)
#         diameter_right = self.diameterOfBinaryTree(root.right)
        
#         # Return the maximum of the three
#         return max(diameter_through_root, diameter_left, diameter_right)

    
#     def height(self, root): 
#         if root is None:
#             return 0 

#         return 1 + max(self.height(root.left),  self.height(root.right))


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0  
        self.height(root)
        
        return self.max_diameter
    
    def height(self, root): 
        if root is None:
            return 0 
        
        # operate on left , right tree
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        
        # update global param
        self.max_diameter = max(self.max_diameter, left_height + right_height)
        
        # Return height of this subtree
        return 1 + max(left_height, right_height)