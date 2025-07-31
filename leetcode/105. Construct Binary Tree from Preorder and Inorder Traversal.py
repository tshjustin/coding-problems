# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        2 Facts to observe: 

        -------------------------
        1. First value in pre-order traversal is always the root (Since we look at the root first, then left , right)

        [3 ,9, 20, 15, 7]

        3 => Root 
        Now that we have built the first level, 
        9 => Root of the left subtree | [9, 20, 15, 7]
        20 => Root of the right subtree [20, 15, 7]

        Note the recurisve nature 

        But how do we know what array makes up what the left / right tree ? This is where the in-order array tells us       
        --------------------------

        2. First value in in-order traversal is always the most left node. 

        We know that 3 is the root, hence we remove from the first list 

        Now we find the same 3 in the in-order array.  We then remove it. => [9, , 15, 20, 7]
        Notice that this is convinient for us, since all elements of the left array is in the left subtree, all elements in the right is the right subtree

        Hence using the first array again, we create a partition =>  [3 ,9, || 20, 15, 7]
        ---------------------------

        Now we create the left subtree first 

        9 => Only node in the left subtree 

        15,20,7 => Reserved for the right subtree

        Repeat the same process => Recursive ! 



        Steps in pseudo code: 

        1. First array , find the first element that tells us this is the root 

        2. Second array, find the same element, this tells us what arrays goes to the left and right tree 

        3. Create a partition in the first array 

        4. Create the tree

        5. Recurse for the right subtree 
        """

        if not preorder or not inorder: 
            return None

        # from the first array, find the first element 
        root = TreeNode(preorder[0])

        # now find the position of the root node in the second array
        # call it mid since we will partition base on this 
        mid =  inorder.index(preorder[0])

        # Now we create the left subtree
        # we need to pass in the new subarrays -> preorder + inorder trancuated  
        # mid tells us the index, which also tells us how many nodes we want in the left subtree
        # look at the example
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])

        # we need all the values after the mid point
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root 

        """
        Note that we are building the tree from the bottom, meaning while we call from the start node,
        we will go all the way down to the left tree, build it... 

        then once we hit the root node, for this current node, we have already build its left subtree


        """




        