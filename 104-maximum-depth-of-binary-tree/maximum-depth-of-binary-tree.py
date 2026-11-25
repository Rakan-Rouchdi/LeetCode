# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):

        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return 0
        # if its a missing child (root.left/right == None) or tree is empty 
        # there is no node
    
        leftDepth = self.maxDepth(root.left) # check how many nodes is on the left subtree
        rightDepth = self.maxDepth(root.right) # check how many nodes is on the right subtree

        return 1 + max(leftDepth, rightDepth) # take the max between the 2 and add the current node we are on 

        