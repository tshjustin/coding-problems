# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Find the base case 

        Apply on left sub tree

        Apply on right sub tree 

        Combine result 

        --------------------------
        For the first case: 
            Look at the node = 3

            left sub tree height = 1
            right sub tree height = 2 
            diff height = | -1 | = 1 <= 1 => thus balanced 

            Perform the check for all the subtrees  


        For each of the nodes: 
            check the height of its sub trees - That is the max height of left - max height of right 

            if violate:
                return 

            else continue 
        """

        if not root:
            # node with no child is balanced 
            return True

        # Now i am thinking of how to calculate the heights 
        # should i go all the way down - calculate ? 
        # but the height function takes care of that for me - So what should i put in ? 
        # i need to track the height, and also the boolean. Should i modify ?  


        # to answer the qustions above: 
        # i should go all the way down to calculate - This means to calcuialte for each node - The height function does the calcuilateion for a current node, by going throguh all nodes 
        # tracking of height can be done to make it one pass , rather than 2 as in the current code 

        # this condition helps with checking of the height # in efficient 
        if abs(self.height(root.left) - self.height(root.right)) > 1:
            return False 

        # check for all the nodes ! 
        return self.isBalanced(root.left) and self.isBalanced(root.right) 
        

    def height(self, root): 
        """
        For height, a nice way to think about it is that each node have an assoicatied height to it (sub cases)

        This means for a basic 3-node tree, the below operation is easy to understand 

        To understand the max, think of 

                1
              /   \
            2      4
           /
          3 
        """
        if root is None: 
            return 0 
        
        left_height = self.height(root.left)
        right_height = self.height(root.right)

        return 1 + max(left_height, right_height) 
        