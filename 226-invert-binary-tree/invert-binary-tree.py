# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root: # if the root is missing
            return None # return none

        # swap the children of the node 
        tmp = root.left # save the original left child
        root.left = root.right # set the left child to the right child
        root.right = tmp # set the right child to the left child

        self.invertTree(root.right) # invert the left subtree first
        self.invertTree(root.left) # then invert the right subtree

        return root # return the root of the inverted tree
        
        # Time: O(n), where n is the number of nodes. We visit each node once.
        # Space: O(h), where h is the tree height, for the recursive call stack.
        # Worst-case space: O(n) if every node has just one child except the leaf.